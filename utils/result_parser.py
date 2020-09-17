import logging


def parse_musicbrainz_result(recording):
    mbid = ""
    title = ""
    album_artist = ""
    album = ""
    contributing_artists = []
    tracknumber = ""
    release_date = ""
    length = ""
    tags = [""]

    try:

        mbid = recording["id"]
        title = recording["title"]
        length = recording["length"]

        for artist_credit in recording["artist-credit"]:
            try:
                contributing_artists.append(artist_credit["artist"]["name"])
            except TypeError as type_error:
                logging.warning(
                    f"Not a serious warning. This was expected. Encountered value {artist_credit} in array of "
                    f"artist-credit dictionaries.This key will just be skipped")

        release = recording['release-list'][0]
        album_artist = release['artist-credit-phrase']
        release_date = release['date']
        album = release['title']
        tracknumber = release['medium-list'][0]['track-list'][0]['position']

        if album_artist == "Various Artists":
            album_artist = contributing_artists[0]

    except KeyError as key_error:
        logging.warning(f"Key {key_error.args} not found .No biggie just ignoring and moving ahead.")

    finally:
        return {"mbid": mbid, "title": title, "album": album, "album_artist": album_artist,
                "contributing_artists": contributing_artists, "tracknumber": tracknumber, "release_date": release_date,
                "length": length, "tags": tags}
