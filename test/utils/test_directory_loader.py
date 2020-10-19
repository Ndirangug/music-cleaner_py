import utils.directory_loader as dloader


def test_directory_loader():
    directory = "/media/georgen/LOCAL DISK/George_Ndirangu/Learning/py/accoustid-music-cleaner/test-res"

    expected = [
        "/media/georgen/LOCAL DISK/George_Ndirangu/Learning/py/accoustid-music-cleaner/test-res/preserve/(10) Man of Your Word (feat. Chandler Moore & KJ Scriven) - Maverick City _ TRIBL - YouTube-converted.mp3",
        "/media/georgen/LOCAL DISK/George_Ndirangu/Learning/py/accoustid-music-cleaner/test-res/preserve/(10) Promises (feat. Joe L Barnes & Naomi Raine) - Maverick City _ TRIBL - YouTube-converted.mp3",
        "/media/georgen/LOCAL DISK/George_Ndirangu/Learning/py/accoustid-music-cleaner/test-res/preserve/AUD-20200510-WA0003.mp3",
        "/media/georgen/LOCAL DISK/George_Ndirangu/Learning/py/accoustid-music-cleaner/test-res/preserve/AUD-20200510-WA0004.mp3",
        "/media/georgen/LOCAL DISK/George_Ndirangu/Learning/py/accoustid-music-cleaner/test-res/preserve/AUD-20200511-WA0000.mp3",
        "/media/georgen/LOCAL DISK/George_Ndirangu/Learning/py/accoustid-music-cleaner/test-res/preserve/Heaven_s_Secrets_WILDER_TRIBL_Music.hd.ogg",
        "/media/georgen/LOCAL DISK/George_Ndirangu/Learning/py/accoustid-music-cleaner/test-res/preserve/King_of_My_Heart_Steffany_Gretzinger_Jeremy_Riddle_Mome.hd.ogg",
        "/media/georgen/LOCAL DISK/George_Ndirangu/Learning/py/accoustid-music-cleaner/test-res/preserve/Steffany_Gretzinger_More_To_Me_with_Chandler_Moore_Offi.hd.mp3",
        "/media/georgen/LOCAL DISK/George_Ndirangu/Learning/py/accoustid-music-cleaner/test-res/preserve/Steffany_Gretzinger_This_Close_with_Chandler_Moore_Offi.hd.mp3",
        "/media/georgen/LOCAL DISK/George_Ndirangu/Learning/py/accoustid-music-cleaner/test-res/preserve/(10) Man of Your Word (feat. Chandler Moore & KJ Scriven) - Maverick City _ TRIBL - YouTube-converted.mp3",
        "/media/georgen/LOCAL DISK/George_Ndirangu/Learning/py/accoustid-music-cleaner/test-res/preserve/(10) Promises (feat. Joe L Barnes & Naomi Raine) - Maverick City _ TRIBL - YouTube-converted.mp3",
        "/media/georgen/LOCAL DISK/George_Ndirangu/Learning/py/accoustid-music-cleaner/test-res/preserve/AUD-20200510-WA0003.mp3",
        "/media/georgen/LOCAL DISK/George_Ndirangu/Learning/py/accoustid-music-cleaner/test-res/preserve/AUD-20200510-WA0004.mp3",
        "/media/georgen/LOCAL DISK/George_Ndirangu/Learning/py/accoustid-music-cleaner/test-res/preserve/AUD-20200511-WA0000.mp3",
        "/media/georgen/LOCAL DISK/George_Ndirangu/Learning/py/accoustid-music-cleaner/test-res/preserve/Heaven_s_Secrets_WILDER_TRIBL_Music.hd.ogg",
        "/media/georgen/LOCAL DISK/George_Ndirangu/Learning/py/accoustid-music-cleaner/test-res/preserve/King_of_My_Heart_Steffany_Gretzinger_Jeremy_Riddle_Mome.hd.ogg",
        "/media/georgen/LOCAL DISK/George_Ndirangu/Learning/py/accoustid-music-cleaner/test-res/preserve/Steffany_Gretzinger_More_To_Me_with_Chandler_Moore_Offi.hd.mp3",
        "/media/georgen/LOCAL DISK/George_Ndirangu/Learning/py/accoustid-music-cleaner/test-res/preserve/Steffany_Gretzinger_This_Close_with_Chandler_Moore_Offi.hd.mp3",
    ]

    actual = dloader.load_file_paths(directory)

    expected.sort() == actual.sort()
