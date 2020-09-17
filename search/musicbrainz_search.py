import logging

import musicbrainzngs

from musicfile.musicfile import MusicFile


class MusicBrainzLookupError(Exception):
    def __init__(self, message):
        self._message = message


musicbrainzngs.set_useragent("muusic-cleaner", "0.1")


def search(musicfile: MusicFile):
    musicbrainzngs.set_useragent("muusic-cleaner", "0.1")

    # try:
    #     result = musicbrainzngs.search_recordings("endless alleluia cory asbury")
    # except musicbrainzngs.WebServiceError as exc:
    #     print("Something went wrong with the request: %s" % exc)
    # else:
    #     for v in (result['recording-list'][1]['artist-credit']):
    #         print(v)


def lookup(musicbrainz_id):
    try:
        return musicbrainzngs.get_recording_by_id(musicbrainz_id,
                                                  includes=["artists", "releases", "artist-credits", "tags",
                                                            "instrument-rels", "media"])
    except musicbrainzngs.WebServiceError as exc:
        raise MusicBrainzLookupError("Something went wrong with the request: %s" % exc)


def parse_musicbrainz_result(musicbrainz_dict):
    recording = musicbrainz_dict["recording"]

    # for key in recording:
    #     print(key)
    #     pprint.pprint(recording[key])
    #     print()

    mbid = recording["id"]
    title = recording["title"]
    length = recording["length"]
    contributing_artists = []
    album_artist = ""
    album = ""
    tags = []
    tracknum = 0
    release_date = ""

    for artist_credit in recording["artist-credit"]:
        try:
            contributing_artists.append(artist_credit["artist"]["name"])
        except TypeError as exec:
            logging.warning(artist_credit, exec.__cause__)

    release = recording['release-list'][0]
    album_artist = release['artist-credit-phrase']
    release_date = release['date']
    album = release['title']
    tracknum = release['medium-list'][0]['track-list'][0]['position']

    if album_artist == "Various Artists":
        album_artist = contributing_artists[0]

    print(mbid, title, length, contributing_artists, album_artist, album, tracknum, release_date)
