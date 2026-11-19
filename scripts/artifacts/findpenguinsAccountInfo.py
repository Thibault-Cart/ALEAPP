__artifacts_v2__ = {
    "findPenguins_accountInfo": {
        "name": "Find Penguins - Account Information",
        "description": "Reports the account information of the logged-in user.",
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
def findPenguins_accountInfo(context):
    files_found = context.get_files_found()
    source_path = get_file_path(files_found, "fp-local-database")

    query = """
        SELECT u.user_id,u.name,u.profile_url,u.homebase,u.bio,u.tagline,u.website,
               u.followers_total,u.following_total,u.stats_json
        FROM users u
        WHERE u.user_id=(SELECT user_id FROM user_logged_in_table LIMIT 1);
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
    )
    return data_headers, data_list, source_path
