import logging

import search.accoustid_search as accoustid
import utils.directory_loader as dloader
from utils.file_loader import music_file_factory, CouldNotMakeMusicFile
from utils.queue import Queue, QueueItem

# directory = "/media/georgen/LOCAL DISK/George_Ndirangu/Learning/py/music-cleaner/test-res/tinker"
directory = "/media/georgen/LOCAL DISK/George_Ndirangu/Music/"

list_of_paths = dloader.load_file_names(directory)

processing_queue = Queue()

for path in list_of_paths:
    try:
        music_file = music_file_factory(path)
        processing_queue.push(QueueItem(music_file))
    except CouldNotMakeMusicFile as could_not_make_musicfile_exception:
        logging.warning(could_not_make_musicfile_exception)

for item in processing_queue.get_items():
    accoustid.search(item.music_file)
