__artifacts_v2__ = {
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
    }
}

from scripts.ilapfuncs import (
    artifact_processor,
    get_file_path,
    get_sqlite_db_records,
    null_absent_columns,
)


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
