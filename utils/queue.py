import logging
from enum import Enum
from typing import List

from musicfile.musicfile import MusicFile
from utils.file_loader import CouldNotMakeMusicFile, music_file_factory


class QueueItemStatus(Enum):
    WAITING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILED = 4


class QueueItem:
    def __init__(self, music_file: MusicFile, status=QueueItemStatus.WAITING):
        self.music_file = music_file
        self.status = status

    def update_status(self, status: QueueItemStatus):
        self.status = status


class Queue:

    def __init__(self, items: List[QueueItem] = list()):
        self.items = items
        self.sorted = False

    def push(self, item: QueueItem):
        self.items.append(item)

    def pop(self, index):
        self.items.pop(index)

    def get_item(self, index: int) -> QueueItem:
        return self.items[index]

    def get_items(self) -> List[QueueItem]:
        return self.items

    def sort(self):
        # TODO sort here
        self.sorted = True

    @staticmethod
    def populate_queue(list, queue):
        for path in list:
            try:
                music_file = music_file_factory(path)
                queue.push(QueueItem(music_file))
            except CouldNotMakeMusicFile as could_not_make_musicfile_exception:
                logging.warning(could_not_make_musicfile_exception)
