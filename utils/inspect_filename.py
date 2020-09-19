import re


class FilenameNotUseful(Exception):
    def __init__(self, message):
        self._message = message


def check_filename_not_useful(filename):
    if re.match(r'aud-[0-9]', filename.lower()):
        raise FilenameNotUseful(
            f"This filename {filename} is probably a computer generated string. It may not be useful for searching")
