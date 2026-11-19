__artifacts_v2__ = {
    "findPenguins_images": {
        "name": "Find Penguins - Images",
        "description": "Reports photo attachments on the logged-in user's footprints and the cached image when found.",
        "author": "@ThibaultCart",
        "creation_date": "2026-11-19",
        "last_update_date": "2026-11-19",
        "requirements": "none",
        "category": "Find Penguins",
        "notes": "Attachments are joined to footprints and filtered by the user_id in user_logged_in_table. A cached image is matched by the lowercase SHA-256 of sizes_m_s_url encoded as UTF-8, followed by .0; filename is the logical filename, not the cache filename. This cache mapping has not been validated against a real FindPenguins extraction. Rows remain present when no unique cache file is found, with the Cached Image column blank. Unmatched cache files are not reported because their association with the logged-in user's footprints cannot be established.",
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
from scripts.ilapfuncs import (
    artifact_processor,
    get_sqlite_db_records,
    logfunc,
    null_absent_columns,
    check_in_media,
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
def findPenguins_images(context):
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
        SELECT
            datetime(a.timestamp / 1000, 'unixepoch') AS image_date,
            f.dateLocal AS publication_date,
            f.footprint_id,
            f.name AS publication_name,
            f.text AS publication_text,
            f.place_name,
            f.country_code,
            f.country_name,
            t.trip_id,
            t.name AS trip_name,
            a.filename,
            a.caption,
            a.attachment_position,
            a.lat AS image_lat,
            a.lng AS image_lng,
            a.sizes_m_s_url AS image_url
        FROM attachments AS a
        JOIN footprints AS f
            ON f.footprint_id = a.footprint_id
        LEFT JOIN trips AS t
            ON t.trip_id = f.trip_id
        WHERE f.user_id = (
            SELECT user_id
            FROM user_logged_in_table
            LIMIT 1
        )
        AND a.type = 'photo'
        AND a.sizes_m_s_url IS NOT NULL
        ORDER BY f.date_utc ASC, a.attachment_position ASC;
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
            media_reference = ""
            image_url = record[-1]
            if container is not None and isinstance(image_url, str) and image_url:
                cache_name = hashlib.sha256(image_url.encode("utf-8")).hexdigest() + ".0"
                candidates = cache_index.get((container, cache_name), [])
                if len(candidates) == 1:
                    media_path = candidates[0]
                    source_paths.add(media_path)
                    media_reference = check_in_media(
                        media_path,
                        name=record[10] or cache_name,
                    ) or ""
                elif len(candidates) > 1:
                    logfunc(
                        f"Find Penguins image cache match is ambiguous for "
                        f"{context.get_relative_path(source_path)}: {cache_name}"
                    )
            data_list.append(tuple(record) + (media_reference,))

    data_headers = (
        "Image Timestamp",
        "Publication Date",
        "Footprint ID",
        "Publication Name",
        "Publication Text",
        "Place Name",
        "Country Code",
        "Country Name",
        "Trip ID",
        "Trip Name",
        "Image Filename",
        "Image Caption",
        "Attachment Position (as stored)",
        "Image Latitude (as stored)",
        "Image Longitude (as stored)",
        "Image URL - Small Size",
        ("Cached Image", "media"),
    )
    return data_headers, data_list, "\n".join(sorted(source_paths))
