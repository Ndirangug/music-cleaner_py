import utils.filename_splitter as fsplitter


def test_split():
    text = "a boy was going"
    expected = ["a boy was going", "a boy was", "boy was going", "a boy", "boy was", "was going", "a", "boy", "was",
                "going"]
    actual = fsplitter.split(text)
    assert expected == actual


def test_cleanup():
    text = " 10A# %54 boy @ was going  "
    expected = "a boy was going"
    actual = fsplitter.cleanup(text)

    assert expected == actual


def test_get_file_name():
    absolute_path = "/home/georgen/George_Ndirangu/Learning/py/music-cleaner/test-res/tinker/(10) Man of Your Word (" \
                    "feat. Chandler Moore & KJ Scriven) - Maverick City _ TRIBL - YouTube-converted.mp3 "
    expected = "(10) Man of Your Word (feat. Chandler Moore & KJ Scriven) - Maverick City _ TRIBL - YouTube-converted"
    actual = fsplitter.get_file_name(absolute_path)

    assert expected == actual
