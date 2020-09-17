import mutagen

from musicfile.musicfile import MusicFile, AudioFormat, UnsupportedAudioFormat


class CouldNotMakeMusicFile(Exception):
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
            return CouldNotMakeMusicFile(f"Mutagen apparently read(or tried to) file but mutagen.File(file_path) "
                                         f"returned None instead of FileType. \n Filepath: {file_path}")
    except mutagen.MutagenError as mutagen_error:
        return CouldNotMakeMusicFile(f"A mutagen error occurred. File not read successfully. File: {file_path} \n "
                                     f"MutagenError: {mutagen_error}")
