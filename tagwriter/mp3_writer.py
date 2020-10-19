from mutagen.mp3 import EasyMP3

from tagwriter.utils import write_to_audio_dict


def write_to_file(music_file):
    audio = EasyMP3(music_file.file_path)
    write_to_audio_dict.write(audio, music_file)
