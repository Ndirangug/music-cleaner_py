import logging

from mutagen.oggopus import OggOpus
from mutagen.oggvorbis import OggVorbis

from tagwriter.utils import write_to_audio_dict
from utils.audio_format import AudioFormat


def write_to_file(music_file):
    if music_file.audioformat == AudioFormat.OGGOPUS:
        audio = OggOpus(music_file.file_path)
        write_to_audio_dict.write(audio, music_file)

    elif music_file.audioformat == AudioFormat.OGGVORBIS:
        audio = OggVorbis(music_file.file_path)
        write_to_audio_dict.write(audio, music_file)

    else:
        logging.warning("Neither ogg vorbis nor opus. Can't write tags")
