from typing import List

from musicfile.musicfile import MusicFile


def on_success(success_list: List[MusicFile], music_file: MusicFile):
    music_file.save_to_disk()
    success_list.append(music_file)


def on_fail(fails_list: List[MusicFile], music_file):
    fails_list.append(music_file)
