import logging

import utils.directory_loader as dloader
import search.accoustid_search as accoustid
from utils.file_loader import music_file_factory, CouldMakeMusicFile
from utils.queue import Queue, QueueItem

# directory = "/media/georgen/LOCAL DISK/George_Ndirangu/Learning/py/music-cleaner/test-res/tinker"
directory = "/media/georgen/LOCAL DISK/George_Ndirangu/Music/"


list_of_paths = dloader.load_file_names(directory)


processing_queue = Queue()

for path in list_of_paths:
   try:
       music_file = music_file_factory(path)
       processing_queue.push(QueueItem(music_file))
   except CouldMakeMusicFile as exc:
        logging.warning(exc)

for item in processing_queue.get_items():
    accoustid.search(item.music_file)
