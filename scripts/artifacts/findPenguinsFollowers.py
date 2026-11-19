__artifacts_v2__ = {
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
    }
}

from scripts.ilapfuncs import artifact_processor, get_file_path, get_sqlite_db_records


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
