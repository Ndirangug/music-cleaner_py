import logging
from typing import Optional

import acoustid
import musicbrainzngs
from beeprint import pp

import search.accoustid.accoustid_search as accoustid
import utils.directory_loader as dloader
from musicfile.musicfile import MusicFile
from search.musicbrainz import musicbrainz_search
from utils.queue import Queue, QueueItemStatus

# directory = "/media/georgen/LOCAL DISK/George_Ndirangu/Learning/py/music-cleaner/test-res/tinker"
directory = "/media/georgen/LOCAL DISK/George_Ndirangu/Music/"

list_of_paths = dloader.load_file_paths(directory)

processing_queue = Queue()

Queue.populate_queue(list_of_paths, processing_queue)

for item in processing_queue.get_items():
    item.update_status(QueueItemStatus.PROCESSING)
    result: Optional[MusicFile] = accoustid.search(item.music_file)

    if isinstance(result, MusicFile):
        item.update_status(QueueItemStatus.SUCCESS)
        pp(result)
    elif isinstance(result, acoustid.WebServiceError):
        logging.warning(f"Network error encountered. Will try to handle this another day.For now moving on \n {result}")
    else:
        # fallback to the next searching method
        logging.warning("fallback to the next searching method ")
        result = musicbrainz_search.search(item.music_file)

        if isinstance(result, MusicFile):
            item.update_status(QueueItemStatus.SUCCESS)
            pp(result)
        elif isinstance(result, musicbrainzngs.WebServiceError):
            logging.warning(
                f"Network error encountered. Will try to handle this another day.For now moving on \n {result}")
        else:
            item.update_status(QueueItemStatus.FAILED)
            logging.warning(f"Both accoustid and mb failed for file {item.music_file.file_path}. Maybe check network")
