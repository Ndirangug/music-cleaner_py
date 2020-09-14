from utils.pre_processor import AudioFormat
from enum import Enum
from musicfile.musicfile import MusicFile

class QueueItemStatus(Enum):
    WAITING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILED = 4

class Queue:
    def __init__(self, items: list()):
        self.items = items

    def push(self, item: QueueItem):
        self.items.append(item)  

    def pop(self, index: int):
        self.items.pop(index = -1)    

    def get_item(self, index: int):
        return self.items[index]

    def get_items(self):
        return self.items    

class QueueItem:
    def __init__(self, music_file: MusicFile, status = QueueItemStatus.WAITING):
        self.music_file = music_file  
        self.status = status

    def update_status(self, status: QueueItemStatus):
        self.status = status
            