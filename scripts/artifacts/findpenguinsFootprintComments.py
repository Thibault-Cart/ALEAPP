__artifacts_v2__ = {
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
    }
}

from scripts.ilapfuncs import artifact_processor, get_file_path, get_sqlite_db_records


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
