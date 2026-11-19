__artifacts_v2__ = {
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
    }
}

from scripts.ilapfuncs import artifact_processor, get_file_path, get_sqlite_db_records


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
