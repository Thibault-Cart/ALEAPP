__artifacts_v2__ = {
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
    }
}

from scripts.ilapfuncs import artifact_processor, get_file_path, get_sqlite_db_records


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
