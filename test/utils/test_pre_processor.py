import mutagen
from utils.pre_processor import *

def test_file_info():        
    try:
       file_path = "/media/georgen/LOCAL DISK/George_Ndirangu/Learning/py/music-cleaner/test-res/tinker/(10) Man of Your Word (feat. Chandler Moore & KJ Scriven) - Maverick City _ TRIBL - YouTube-converted.mp3"
       info = file_info(file_path)
       assert info['audioformat'] == AudioFormat.MP3

       file_path = "/media/georgen/LOCAL DISK/George_Ndirangu/Learning/py/music-cleaner/test-res/tinker/Heaven_s_Secrets_WILDER_TRIBL_Music.hd.ogg"
       info = file_info(file_path)
       assert info['audioformat'] == AudioFormat.OGGOPUS
       
    except FileNotFoundError as file_not_found_error:
       print(file_not_found_error)
     