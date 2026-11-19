__artifacts_v2__ = {
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
    }
}

from scripts.ilapfuncs import artifact_processor, get_file_path, get_sqlite_db_records


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
