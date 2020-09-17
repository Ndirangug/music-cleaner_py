import glob
import os.path as op


def load_file_paths(directory: str):
    if directory.endswith('/'):
        directory = directory.rstrip('/')

    paths_list = glob.glob(directory + '/**', recursive=True)
    return list(filter(isfile, paths_list))


def isfile(path):
    return op.isfile(path)
