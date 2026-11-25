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
    },
    "findPenguins_followers": {
        "name": "Find Penguins - Follower ",
        "description": "Reports user records that are following the logged-in user.",
        "author": "@ThibaultCart",
        "creation_date": "2026-11-19",
        "last_update_date": "2026-11-19",
        "requirements": "none",
        "category": "Find Penguins",
        "notes": "Following State and Follower State are reported as stored; their numeric meanings "
                 "have not been verified. In the supplied query output, Email and Follow Request "
                 "Count were blank for all four rows; other extractions have not been checked.",
        "paths": (
            "*/com.findpenguins.app/databases/fp-local-database*",
        ),
        "output_types": ["html", "tsv", "lava"],
        "artifact_icon": "user",
    },
    "findPenguins_following": {
        "name": "Find Penguins - Account followed",
        "description": "Reports user records that are followed by the logged-in user.",
        "author": "@ThibaultCart",
        "creation_date": "2026-11-19",
        "last_update_date": "2026-11-19",
        "requirements": "none",
        "category": "Find Penguins",
        "notes": "Following State and Follower State are reported as stored; their numeric meanings have not been verified. In the supplied query output, Email and Follow Request Count were blank for all four rows; other extractions have not been checked.",
        "paths": (
            "*/com.findpenguins.app/databases/fp-local-database*",
        ),
        "output_types": ["html", "tsv", "lava"],
        "artifact_icon": "user",
    },
    "findPenguins_tripsList": {
        "name": "Find Penguins - Trips List",
        "description": "Reports the list of trips for the logged-in user.",
        "author": "@ThibaultCart",
        "creation_date": "2026-11-19",
        "last_update_date": "2026-11-19",
        "requirements": "none",
        "category": "Find Penguins",
        "paths": (
            "*/com.findpenguins.app/databases/fp-local-database*",
        ),
        "output_types": "standard",
        "artifact_icon": "report",
    },
    "findPenguins_footprint": {
        "name": "Find Penguins - Footprint ",
        "description": "Reports footprint records joined to trips for the logged-in user.",
        "author": "@ThibaultCart",
        "creation_date": "2026-11-19",
        "last_update_date": "2026-11-19",
        "requirements": "none",
        "category": "Find Penguins",
        "notes": "Reads the app database as stored. Missing columns in older database versions are left blank; numeric fields are not given meanings beyond their stored values.",
        "paths": (
            "*/com.findpenguins.app/databases/fp-local-database*",
        ),
        "output_types": "standard",
        "artifact_icon": "report",
    },
    "findPenguins_footprintComments": {
        "name": "Find Penguins -  Footprint Comments",
        "description": "Reports the list of comments and replies for the logged-in user's footprints.",
        "author": "@ThibaultCart",
        "creation_date": "2026-11-19",
        "last_update_date": "2026-11-19",
        "requirements": "none",
        "category": "Find Penguins",
        "paths": (
            "*/com.findpenguins.app/databases/fp-local-database*",
        ),
        "output_types": "standard",
        "artifact_icon": "report",
    },
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
    },
    "findPenguins_imageVideoDump": {
        "name": "Find Penguins - Cached Images and Videos",
        "description": "Reports media files found in the Find Penguins image, picture, HTTP, "
                       "and downloaded-video caches.",
        "author": "@ThibaultCart",
        "creation_date": "2026-11-19",
        "last_update_date": "2026-11-24",
        "requirements": "none",
        "category": "Find Penguins",
        "notes": "Files are included individually, including cache files that cannot be identified "
                 "as media by their content. The media type is detected from the file contents, not "
                 "the cache filename. The .exo files are surfaced as stored; this artifact does not "
                 "reassemble segmented ExoPlayer media. Where the required cache index and spans are "
                 "available, the separate ExoPlayer - Rejoined Cached Media artifact may reconstruct "
                 "playable media. No database association is made for these cache files.",
        "paths": (
            "*/com.findpenguins.app/cache/image_manager_disk_cache/*.0",
            "*/com.findpenguins.app/files/downloaded_videos/2/*.exo",
            "*/com.findpenguins.app/cache/pictures/*",
            "*/com.findpenguins.app/cache/http/*.1",
        ),
        "output_types": "standard",
        "artifact_icon": "photo",
    },
    "findPenguins_privateMessage": {
        "name": "Find Penguins - Private Messages",
        "description": "Reports the list of private messages for the logged-in user.",
        "author": "@ThibaultCart",
        "creation_date": "2026-11-19",
        "last_update_date": "2026-11-19",
        "requirements": "none",
        "category": "Find Penguins",
        "paths": (
            "*/com.findpenguins.app/databases/fp-local-database*",
        ),
        "output_types": "standard",
        "artifact_icon": "report",
    },
}

import hashlib
import os

from scripts.artifacts.storagePathViews import canonical_path, unique_files
from scripts.filetype import guess_extension, guess_mime
from scripts.ilapfuncs import (
    artifact_processor,
    check_in_media,
    get_file_path,
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


@artifact_processor
def findPenguins_followers(context):
    files_found = context.get_files_found()
    source_path = get_file_path(files_found, "fp-local-database")

    query = """
        SELECT user_id, name, email, profile_url, following_state, follower_state,
               followers_total, following_total
        FROM users
        WHERE follower_state = 1
        ORDER BY name;
    """

    data_list = []
    db_records = get_sqlite_db_records(source_path, query)
    for record in db_records:
        data_list.append(tuple(record))

    data_headers = (
        "User ID",
        "Name",
        "Email",
        "Profile URL",
        "Following State (as stored)",
        "Follower State (as stored)",
        ("Followers Total", "number"),
        ("Following Total", "number"),
        
    )
    return data_headers, data_list, source_path


@artifact_processor
def findPenguins_following(context):
    files_found = context.get_files_found()
    source_path = get_file_path(files_found, "fp-local-database")

    query = """
        SELECT
    u.user_id,
    u.name,
    u.following_state,
    u.follower_state,
    u.followers_total,
    u.following_total
FROM follow_list_entries AS fle
JOIN users AS u
    ON u.user_id = fle.user_id
WHERE fle.list_owner_id = (
    SELECT user_id
    FROM user_logged_in_table
    LIMIT 1
)
AND fle.list_type = 'following'
ORDER BY u.name;
    """

    data_list = []
    db_records = get_sqlite_db_records(source_path, query)
    for record in db_records:
        data_list.append(tuple(record))

    data_headers = (
        "User ID",
        "Name",
        "Following State (as stored)",
        "Follower State (as stored)",
        ("Followers Total", "number"),
        ("Following Total", "number"),
    )
    return data_headers, data_list, source_path


@artifact_processor
def findPenguins_tripsList(context):
    files_found = context.get_files_found()
    source_path = get_file_path(files_found, "fp-local-database")

    query = """
       SELECT
    t.trip_id,
    t.user_id,
    t.name,
    t.description,
    t.description_default,
    t.start_date,
    t.end_date,
    t.privacy,
    t.stats_footprints AS nb_footprint,
    t.stats_countries AS nb_countries,
    t.stats_days AS nb_days,
    t.stats_distance AS distance_traveled,
    t.stats_distance_unit AS distance_unit,
    t.countries_list
FROM trips AS t
WHERE t.user_id = (
    SELECT user_id
    FROM user_logged_in_table
    LIMIT 1
)
ORDER BY t.sort_date DESC;
    """

    data_list = []
    db_records = get_sqlite_db_records(source_path, query)
    for record in db_records:
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
            record[10],
            record[11],
            record[12],
            record[13],
        ))

    data_headers = (
        "Trip ID",
        "User ID",
        "Name",
        "Description",
        "Description Default",
        "Start Date",
        "End Date",
        "Privacy",
        ("Number of Footprints", "number"),
        ("Number of Countries", "number"),
        ("Number of Days", "number"),
        ("Distance Traveled", "number"),
        "Distance Unit",
        "Countries List",
    )
    return data_headers, data_list, source_path


@artifact_processor
def findPenguins_footprint(context):
    files_found = context.get_files_found()
    source_path = get_file_path(files_found, "fp-local-database")

    query = """
     SELECT
   
    t.trip_id,
    t.name AS trip_name,

    f.footprint_id,
    f.user_id,

    f.name AS footprint_name,
    f.text,

    f.dateLocal AS date_local,
    f.date_utc,
    f.day,

    f.place_name,
    f.country_code,
    f.country_name,

    f.lat,
    f.lng,
    f.altitude,

    f.privacy,
    f.is_planned,
    f.off_route,

    f.weather,
    f.weather_temp,

    f.likes_count,
    f.comments_count

  
FROM footprints AS f

JOIN trips AS t
    ON t.trip_id = f.trip_id

WHERE t.user_id = (
    SELECT user_id
    FROM user_logged_in_table
    LIMIT 1
)

ORDER BY
    t.sort_date DESC,
    f.date_utc ASC;
    """

    data_list = []
    db_records = get_sqlite_db_records(
        source_path,
        null_absent_columns(source_path, query),
    )
    for record in db_records:
        data_list.append(tuple(record))

    data_headers = (
        "Trip ID",
        "Trip Name",
        "Footprint ID",
        "User ID",
        "Footprint Name",
        "Text",
        "Date Local",
        "Date UTC",
        "Day",
        "Place Name",
        "Country Code",
        "Country Name",
        "Latitude",
        "Longitude",
        "Altitude",
        "Privacy",
        "Is Planned",
        "Off Route",
        "Weather",
        "Weather Temp",
        ("Likes Count", "number"),
        ("Comments Count", "number"),
    )
    return data_headers, data_list, source_path


@artifact_processor
def findPenguins_footprintComments(context):
    files_found = context.get_files_found()
    source_path = get_file_path(files_found, "fp-local-database")

    query = """
     SELECT
    f.footprint_id,
    f.name AS footprint_name,

    c.comment_id,
    c.parent_id,

    CASE
        WHEN c.parent_id IS NULL THEN 'comment'
        ELSE 'reply'
    END AS comment_type,

    c.user_id AS author_user_id,
    u.name AS author_name,

    c.text AS comment_text,
    c.date AS comment_date,

    datetime(c.insert_date, 'unixepoch') AS insert_date,

    c.status,
    c.editable,
    c.translatable

FROM footprints AS f

JOIN comments AS c
    ON c.footprint_id = f.footprint_id

LEFT JOIN users AS u
    ON u.user_id = c.user_id

WHERE f.user_id = (
    SELECT user_id
    FROM user_logged_in_table
    LIMIT 1
)

ORDER BY
    f.footprint_id,
    COALESCE(c.parent_id, c.comment_id),
    CASE
        WHEN c.parent_id IS NULL THEN 0
        ELSE 1
    END,
    c.insert_date ASC;
    """

    data_list = []
    db_records = get_sqlite_db_records(source_path, query)
    for record in db_records:
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
            record[10],
            record[11],
            record[12],
        ))

    data_headers = (
        "Footprint ID",
        "Footprint Name",
        "Comment ID",
        "Parent ID",
        "Comment Type",
        "Author User ID",
        "Author Name",
        "Comment Text",
        ("Comment Date", "datetime"),
        ("Insert Date", "datetime"),
        "Status",
        "Editable",
        "Translatable"
    )
    return data_headers, data_list, source_path


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


@artifact_processor
def findPenguins_imageVideoDump(context):
    data_list = []
    source_paths = []

    for file_found in unique_files(context):
        file_found = str(file_found)
        if not os.path.isfile(file_found):
            continue

        filename = os.path.basename(file_found)
        mime_type = guess_mime(file_found) or ""
        extension = guess_extension(file_found)
        media = check_in_media(
            file_found,
            name=filename,
            force_type=mime_type or None,
            force_extension=extension,
        ) or ""

        data_list.append((
            filename,
            mime_type,
            os.path.getsize(file_found),
            context.get_relative_path(file_found),
            media,
        ))
        source_paths.append(file_found)

    data_headers = (
        "File Name",
        "Detected MIME Type",
        ("Size (bytes)", "number"),
        "Source Path",
        ("Media", "media"),
    )
    return data_headers, data_list, "\n".join(source_paths)


@artifact_processor
def findPenguins_privateMessage(context):
    files_found = context.get_files_found()
    source_path = get_file_path(files_found, "fp-local-database")

    query = """
     SELECT
    dm.id_api AS message_id,
    dm.chat_id,
    chat_user.name AS chat_with_name,

    dm.sender_user_id,
    sender.name AS sender_name,

    dm.text AS message,
    dm.timestamp,
    dm.unread,
    dm.status

FROM direct_messages AS dm

LEFT JOIN users AS sender
    ON sender.user_id = dm.sender_user_id

LEFT JOIN users AS chat_user
    ON chat_user.user_id = dm.chat_id

ORDER BY
    
    dm.timestamp ASC,dm.chat_id ASC;
    """

    data_list = []
    db_records = get_sqlite_db_records(source_path, query)
    for record in db_records:
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
        ))

    data_headers = (
        "Message ID",
        "Chat ID",
        "Chat With Name",
        "Sender User ID",
        "Sender Name",
        "Message",
        ("Timestamp", "datetime"),
        ("Unread", "boolean"),
        "Status",
    )
    return data_headers, data_list, source_path
