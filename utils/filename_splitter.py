import ntpath
import os
import re


def split(filename: str):
    filename = cleanup(filename)
    filename_array = filename.split(' ')
    return filename_array


def cleanup(filename):
    filename = re.sub(r'[^A-Za-z\s]', '', filename)
    filename = re.sub(r'\s{1,5}', ' ', filename)
    filename = filename.strip()
    filename = filename.lower()
    return filename


def get_file_name(absolute_path):
    filename = ntpath.basename(absolute_path)
    filename = os.path.splitext(filename)[0]
    return filename
