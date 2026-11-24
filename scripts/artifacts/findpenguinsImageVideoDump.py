__artifacts_v2__ = {
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
    }
}

import os

from scripts.artifacts.storagePathViews import unique_files
from scripts.filetype import guess_extension, guess_mime
from scripts.ilapfuncs import artifact_processor, check_in_media


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
