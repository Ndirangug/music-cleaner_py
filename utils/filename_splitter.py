import ntpath
import os
import re
from itertools import combinations


def length_sort(text):
    return len(text)


def split(filename: str):
    filename = cleanup(filename)
    filename_array = filename.split(' ')

    combinations_from_file_name = [filename_array[x:y] for x, y in combinations(
        range(len(filename_array) + 1), r=2)]
    combinations_from_file_name.sort(key=length_sort, reverse=True)

    combinations_from_file_name = [" ".join(combination) for combination in combinations_from_file_name]

    return combinations_from_file_name


def cleanup(filename):
    filename = re.sub(r'[\-\_]', ' ', filename)
    filename = re.sub(r'[^A-Za-z\s]', '', filename)
    filename = re.sub(r'\s{1,5}', ' ', filename)
    filename = filename.strip()
    filename = filename.lower()
    return filename


def get_file_name(absolute_path):
    filename = ntpath.basename(absolute_path)
    filename = os.path.splitext(filename)[0]

    return filename
