import logging

import musicbrainzngs

import utils.filename_splitter as fsplitter
from musicfile.musicfile import MusicFile
from search.musicbrainz.utils.validate_result import validate_result
from utils.inspect_filename import check_filename_not_useful, FilenameNotUseful
from utils.update_musicfile import update_musicfile


class MusicBrainzLookupError(Exception):
    def __init__(self, message):
        self._message = message


musicbrainzngs.set_useragent("music-cleaner", "0.1", "ndirangu.mepawa@gmail.com")


def search(musicfile: MusicFile):
    try:
        filename = fsplitter.get_file_name(musicfile.file_path)
        check_filename_not_useful(filename)
        file_name_fragments = fsplitter.split(filename)
        recording = None

        iterations = 0

        for fragment in file_name_fragments:
            if iterations > 5:
                logging.warning("Crossed 5 iterations...moving on")
                break
            iterations += 1

            try:
                result = musicbrainzngs.search_recordings(fragment)

                found_valid_match, recording = validate_result(result, fragment, file_name_fragments)
                if found_valid_match:
                    update_musicfile(musicfile, recording)
                    return musicfile

            except musicbrainzngs.WebServiceError as web_service_error:
                logging.warning(f"Something went wrong with the request: {web_service_error}")
                return web_service_error
    except FilenameNotUseful as filename_not_useful:
        logging.warning(
            f"FilenameNotUseful exception encountered. No need to continue search.\n Exception: {filename_not_useful}")


def lookup(musicbrainz_id):
    try:
        return musicbrainzngs.get_recording_by_id(musicbrainz_id,
                                                  includes=["artists", "releases", "artist-credits", "tags",
                                                            "instrument-rels", "media"])
    except musicbrainzngs.WebServiceError as web_service_error:
        raise MusicBrainzLookupError(f"Something went wrong with the request: {web_service_error}")
