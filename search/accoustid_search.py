import acoustid
from musicfile.musicfile import MusicFile
import search.musicbrainz_search as mb
import logging

# TODO use .env
apikey = "xZI2oVLvE7"


class AccoustIdNoMatch(Exception):
    def __init__(self, message=""):
        self._message = message


class AccoustLookupError(Exception):
    def __init__(self, message=""):
        self._message = message


def search(musicfile: MusicFile):
    get_musicbrainz_id(musicfile)

    if len(musicfile.musicbrainz_id) > 1:
        lookup_result = mb.lookup(musicfile.musicbrainz_id)
        mb.extract_from_dict(lookup_result)
        # TODO extract results
    else:
        logging.warning("%s", AccoustIdNoMatch)

    return musicfile


def get_musicbrainz_id(musicfile: MusicFile):
    score_cache = 0

    try:

        for score, recording_id, title, artist in acoustid.match(apikey, musicfile.file_path):
            if score > score_cache:
                musicfile.musicbrainz_id = recording_id
                score_cache = score
    except acoustid.FingerprintGenerationError as exc:
        logging.warning("%s", AccoustLookupError(exc))
        logging.warning(musicfile.file_path)

