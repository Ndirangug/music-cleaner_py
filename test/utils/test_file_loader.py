import mutagen
from utils.file_loader import *

def test_file_info():        
    try:
       file_path = "/media/georgen/LOCAL DISK/George_Ndirangu/Learning/py/music-cleaner/test-res/tinker/(10) Man of Your Word (feat. Chandler Moore & KJ Scriven) - Maverick City _ TRIBL - YouTube-converted.mp3"
       music_file = music_file_factory(file_path)
       assert music_file.audioformat == AudioFormat.MP3

       file_path = "/media/georgen/LOCAL DISK/George_Ndirangu/Learning/py/music-cleaner/test-res/tinker/Heaven_s_Secrets_WILDER_TRIBL_Music.hd.ogg"
       music_file = music_file_factory(file_path)
       assert music_file.audioformat == AudioFormat.OGGOPUS
       
    except FileNotFoundError as file_not_found_error:
       print(file_not_found_error)