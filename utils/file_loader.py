import mutagen
import logging
from musicfile.musicfile import MusicFile, AudioFormat, UnsupportedAudioFormat


class CouldMakeMusicFile(Exception):
    def __init__(self, message=""):
        self._message = message


def music_file_factory(file_path):
    try:
        metadata: mutagen.FileType = mutagen.File(file_path)
        if metadata is not None:
            info = str(metadata.info)
            audioformat: AudioFormat = None
            tags = {}

            if metadata.tags is not None:
                tags = metadata.tags

            if info.__contains__('mp3'):
                audioformat = AudioFormat.MP3
            elif info.__contains__('opus'):
                audioformat = AudioFormat.OGGOPUS
            elif info.__contains__('vorbis'):
                audioformat = AudioFormat.OGGVORBIS
            else:
                raise UnsupportedAudioFormat(metadata.info)

            return MusicFile(file_path, audioformat)

        else:
            return CouldMakeMusicFile(file_path + " metadata.info empty")
    except mutagen.MutagenError as mutagen_error:
        return CouldMakeMusicFile("%s \n %s", file_path, mutagen_error)
