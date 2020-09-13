import mutagen
import logging
from enum import Enum

class AudioFormat(Enum):
    MP3 = 1
    OGGOPUS = 2
    OGGVORBIS = 3

class UnsupportedAudioFormat(Exception):
    def __init__(self, message):
        self._message = message
        

def file_info(file_path):
    try:
        metadata: mutagen.FileType = mutagen.File(file_path)
        info = str(metadata.info)
        audioformat: AudioFormat = None
        tags = {}

        if metadata.tags != None:
            tags = metadata.tags       
        
        if info.__contains__('mp3'):
            audioformat = AudioFormat.MP3
        elif info.__contains__('opus'):
            audioformat = AudioFormat.OGGOPUS
        elif info.__contains__('vorbis'):
            audioformat = AudioFormat.OGGVORBIS
        else:
           raise UnsupportedAudioFormat(metadata.info)
         
        return {"audioformat": audioformat, "filepath": file_path, **tags}

    except mutagen.MutagenError as mutagen_error:
        logging.error(mutagen_error)

       