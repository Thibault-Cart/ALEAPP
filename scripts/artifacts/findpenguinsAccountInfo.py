__artifacts_v2__ = {
    "findPenguins_accountInfo": {
        "name": "Find Penguins - Account Information",
        "description": "Reports the account information of the logged-in user and the cached "
                       "profile image when found.",
        "author": "@ThibaultCart",
        "creation_date": "2026-11-19",
        "last_update_date": "2026-11-24",
        "requirements": "none",
        "category": "Find Penguins",
        "notes": "The Profile Image is matched from user_image_sizes_m_s_url by its lowercase "
                 "SHA-256 (UTF-8) filename plus .0 in image_manager_disk_cache. Both the "
                 "user_image_sizes_m_s_url and user_image_sizes_l_url hashes matched cache "
                 "files in the supplied extraction; this artifact displays the m_s image only. "
                 "If no matching m_s cache file exists, the account row remains and the image "
                 "is blank.",
        "paths": (
            "*/com.findpenguins.app/databases/fp-local-database*",
            "*/com.findpenguins.app/cache/image_manager_disk_cache/*.0",
        ),
        "output_types": "standard",
        "artifact_icon": "report",
    }
}

import hashlib

from scripts.artifacts.storagePathViews import canonical_path, unique_files
from scripts.filetype import guess_extension, guess_mime
from scripts.ilapfuncs import (
    artifact_processor,
    check_in_media,
    get_sqlite_db_records,
    logfunc,
    null_absent_columns,
)


def _path_basename(path):
    return str(path).replace("\\", "/").rsplit("/", 1)[-1]


def _container_key(context, path):
    relative_path = str(context.get_relative_path(path)).replace("\\", "/")
    path_parts = relative_path.split("/")
    try:
        package_index = path_parts.index("com.findpenguins.app")
    except ValueError:
        return None
    app_directory = "/".join(path_parts[:package_index + 1])
    return canonical_path(app_directory)[0]


@artifact_processor
def findPenguins_accountInfo(context):
    files_found = [str(path) for path in unique_files(context)]
    database_paths = [
        path for path in files_found
        if _path_basename(path) == "fp-local-database"
    ]
    cache_index = {}
    for path in files_found:
        if not _path_basename(path).endswith(".0"):
            continue
        container = _container_key(context, path)
        if container is not None:
            cache_index.setdefault((container, _path_basename(path)), []).append(path)

    query = """
        SELECT u.user_id,u.name,u.profile_url,u.homebase,u.bio,u.tagline,u.website,
               u.followers_total,u.following_total,u.stats_json,
               u.user_image_sizes_m_s_url
        FROM users u
        WHERE u.user_id=(SELECT user_id FROM user_logged_in_table LIMIT 1);
    """

    data_list = []
    source_paths = set()
    for source_path in database_paths:
        source_paths.add(source_path)
        container = _container_key(context, source_path)
        db_records = get_sqlite_db_records(
            source_path,
            null_absent_columns(source_path, query),
        )
        for record in db_records:
            profile_image = ""
            image_url = record[10]
            if container is not None and isinstance(image_url, str) and image_url:
                cache_name = hashlib.sha256(image_url.encode("utf-8")).hexdigest() + ".0"
                candidates = cache_index.get((container, cache_name), [])
                if len(candidates) == 1:
                    cache_path = candidates[0]
                    mime_type = guess_mime(cache_path)
                    extension = guess_extension(cache_path)
                    media_name = f"Profile Image.{extension}" if extension else "Profile Image"
                    profile_image = check_in_media(
                        cache_path,
                        name=media_name,
                        force_type=mime_type,
                        force_extension=extension,
                    ) or ""
                    source_paths.add(cache_path)
                elif len(candidates) > 1:
                    logfunc(
                        f"Find Penguins profile image cache match is ambiguous for "
                        f"{context.get_relative_path(source_path)}: {cache_name}"
                    )

            data_list.append((
                record[0],
                record[1],
                record[2],
                record[3],
                record[4],
                record[5],
                record[6],
                record[7],
                record[8],
                record[9],
                profile_image,
            ))

    data_headers = (
        "User ID",
        "Name",
        "Profile URL",
        "Homebase",
        "Bio",
        "Tagline",
        "Website",
        "Followers Total",
        "Following Total",
        "Stats JSON",
        ("Profile Image", "media"),
    )
    return data_headers, data_list, "\n".join(sorted(source_paths))
