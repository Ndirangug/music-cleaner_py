import logging
from typing import Optional
import acoustid

import search.accoustid.accoustid_search as accoustid
import utils.directory_loader as dloader
from musicfile.musicfile import MusicFile
from utils.post_search import on_success, on_fail
from utils.queue import Queue, QueueItemStatus
import sys


def main(directories: []):
    # directories = [
    #     # "/media/georgen/LOCAL DISK/George_Ndirangu/Music/",
    #     # "/media/georgen/LOCAL DISK/George_Ndirangu/Videos/Music/",
    #     # "/media/georgen/LOCAL DISK/George_Ndirangu/Learning/py/accoustid-music-cleaner/test-res/tinker"
    # ]

    list_of_paths = []
    completed = []
    failed = []

    for directory in directories:
        list_of_paths += dloader.load_file_paths(directory)

    processing_queue = Queue()
    Queue.populate_queue(list_of_paths, processing_queue)

    for item in processing_queue.get_items():
        item.update_status(QueueItemStatus.PROCESSING)
        result: Optional[MusicFile] = accoustid.search(item.music_file)

        if isinstance(result, MusicFile):
            item.update_status(QueueItemStatus.SUCCESS)
            on_success(completed, item.music_file)
            processing_queue.remove(item)
        elif isinstance(result, acoustid.WebServiceError):
            print(
                f"WARNING: Network error encountered. Will try to handle this another day.For now moving on \n {result}")
        else:
            # fallback to the next searching method
            print("WARNING: fallback to the next searching method ")
            print("WARNING: Musicbrainz search has been disabled for now..until it achives better perforance")
            # result = musicbrainz_search.search(item.music_file)
            #
            # if isinstance(result, MusicFile):
            #     item.update_status(QueueItemStatus.SUCCESS)
            #     on_success(completed, item.music_file)
            #     processing_queue.remove(item)
            # elif isinstance(result, musicbrainzngs.WebServiceError):
            #     logging.warning(
            #         f"Network error encountered. Will try to handle this another day.For now moving on \n {result}")
            # else:
            item.update_status(QueueItemStatus.FAILED)
            on_fail(failed, item.music_file)
            #     processing_queue.remove(item)
            print(f"WARNING: Both accoustid and mb failed for file {item.music_file.file_path}.")

    print("completed...........")
    print(completed)
    print("failed...........")
    print(failed)


if __name__ == "__main__":
    directories_args = []

    for i, arg in enumerate(sys.argv):
        if i == 0:
            continue
        directories_args.append(arg)


    main(directories_args)
