import logging

import musicbrainzngs

from musicfile.musicfile import MusicFile


class MusicBrainzLookupError(Exception):
    def __init__(self, message):
        self._message = message


musicbrainzngs.set_useragent("music-cleaner", "0.1", "ndirangu.mepawa@gmail.com")


def search(musicfile: MusicFile):
    # try:
    #     result = musicbrainzngs.search_recordings("endless alleluia cory asbury")
    # except musicbrainzngs.WebServiceError as exc:
    #     print("Something went wrong with the request: %s" % exc)
    # else:
    #     for v in (result['recording-list'][1]['artist-credit']):
    #         print(v)
    pass


def lookup(musicbrainz_id):
    try:
        return musicbrainzngs.get_recording_by_id(musicbrainz_id,
                                                  includes=["artists", "releases", "artist-credits", "tags",
                                                            "instrument-rels", "media"])
    except musicbrainzngs.WebServiceError as web_service_error:
        raise MusicBrainzLookupError(f"Something went wrong with the request: {web_service_error}")


def parse_musicbrainz_result(musicbrainz_dict):
    recording = musicbrainz_dict["recording"]

    mbid = recording["id"]
    title = recording["title"]
    length = recording["length"]
    contributing_artists = []
    tags = []

    for artist_credit in recording["artist-credit"]:
        try:
            contributing_artists.append(artist_credit["artist"]["name"])
        except TypeError as type_error:
            logging.warning(f"Not a serious warning. This was expected. Encountered value {artist_credit} in array of "
                            f"artist-credit dictionaries.This key will just be skipped")

    release = recording['release-list'][0]
    album_artist = release['artist-credit-phrase']
    release_date = release['date']
    album = release['title']
    tracknumber = release['medium-list'][0]['track-list'][0]['position']

    if album_artist == "Various Artists":
        album_artist = contributing_artists[0]

    return {"mbid": mbid, "title": title, "album": album, "album_artist": album_artist,
            "contributing_artists": contributing_artists, "tracknumber": tracknumber, "release_date": release_date,
            "length": length, "tags": tags}
