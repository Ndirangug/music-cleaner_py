from enum import Enum

class AudioFormat(Enum):
    MP3 = 1
    OGGOPUS = 2
    OGGVORBIS = 3


class UnsupportedAudioFormat(Exception):
    def __init__(self, message):
        self._message = message