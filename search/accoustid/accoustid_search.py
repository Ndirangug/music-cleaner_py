import logging

import acoustid

import search.musicbrainz.musicbrainz_search as mb
from musicfile.musicfile import MusicFile
from utils.update_musicfile import update_musicfile

# TODO use .env
apikey = "xZI2oVLvE7"


class AccoustIdNoMatch(Exception):
    def __init__(self, message=""):
        self._message = message


class AccoustLookupError(Exception):
    def __init__(self, message=""):
        self._message = message


def search(musicfile: MusicFile):
    try:
        get_musicbrainz_id(musicfile)

        if len(musicfile.musicbrainz_id) > 1:
            lookup_result = mb.lookup(musicfile.musicbrainz_id)
            update_musicfile(musicfile, lookup_result["recording"])

        else:
            raise AccoustIdNoMatch("No match found")

        return musicfile

    except acoustid.FingerprintGenerationError as fingerprint_generation_error:
        logging.warning(f"When attempting to generate fingerprint for file {musicfile.file_path} the following error "
                        f"occurred {AccoustLookupError(fingerprint_generation_error.__str__())}")
        return None

    except AccoustIdNoMatch as accoust_id_no_match_exception:
        logging.warning(
            f"A search was probably performed for file {musicfile.file_path} but no conclusive results returned. "
            f"Exception: {accoust_id_no_match_exception}")
        return None

    except mb.MusicBrainzLookupError as musicbrainz_lookup_error:
        logging.warning(f"Accoustid search was successful but an error was encountered while looking up recording "
                        f"details. Exception: {musicbrainz_lookup_error}")
        return None

    except acoustid.WebServiceError as web_service_error:
        logging.warning(f"There was an error probably a network one {web_service_error}")
        return web_service_error


def get_musicbrainz_id(musicfile: MusicFile):
    score_cache = 0

    for score, recording_id, title, artist in acoustid.match(apikey, musicfile.file_path):
        if score > score_cache:
            musicfile.musicbrainz_id = recording_id
            score_cache = score
