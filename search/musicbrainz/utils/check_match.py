import logging

from utils.filename_splitter import cleanup


def check_title_match(title, fragments, threshold):
    # IF at least 3 fragments in title are present in the fragments
    matches_found = 0
    title_does_match = False

    title = cleanup(title)
    logging.warning(f"Prep to validate title {title} using method 2")
    title_fragments = title.split(' ')
    logging.warning(f"title_fragments {title_fragments} ")

    for title_fragment in title_fragments:
        if title_fragment in fragments:
            matches_found += 1
            logging.warning(f"match {matches_found} {title_fragment} in title_fragments")

            if matches_found >= threshold:
                title_does_match = True
                break

        else:
            logging.warning(f"Dint find fragment {title_fragment} in title_fragments")
    return title_does_match


def check_artist_match(recording, fragments):
    artist = ""
    artist_does_match = False
    matches_found = 0

    try:
        artist = recording["artist-credit"][0]["artist"]["name"].lower()

        # IF at least 2 fragments in artist_fragments are present in the fragments
        artist = cleanup(artist)
        artist_fragments = set(artist.split(" "))

        for artist_fragment in artist_fragments:
            if artist_fragment in fragments:
                matches_found += 1
                logging.warning(f"match {matches_found} {artist_fragment} in artist_fragments")

                if matches_found >= 2:
                    artist_does_match = True
                    break

            else:
                logging.warning(f"Dint find fragment {artist_fragment} in title_fragments")

    except KeyError as key_error:
        logging.warning(f"Key {key_error.args} not found. Can't validate with artist")

    return artist_does_match, matches_found


def check_album_match(recording, fragments):
    album = ""
    album_does_match = False
    matches_found = 0

    try:
        album = recording["release-list"][0]['title'].lower()

        # IF at least 2 fragments in album_fragments are present in the fragments
        album = cleanup(album)
        album_fragments = set(album.split(" "))

        for album_fragment in album_fragments:
            if album_fragment in fragments:
                matches_found += 1
                logging.warning(f"match {matches_found} {album_fragment} in album_fragments")

                if matches_found >= 2:
                    album_does_match = True
                    break

            else:
                logging.warning(f"Dint find fragment {album_fragment} in title_fragments")

    except KeyError as key_error:
        logging.warning(f"Key {key_error.args} not found. Can't validate with album name")

    return album_does_match, matches_found


def check_album_artist_title_match(recording, fragments):
    title = recording["title"].lower()

    title_matches_fragments = check_title_match(title, fragments, threshold=1)
    artist_matches_fragments, matches_found_artist = check_artist_match(recording, fragments)
    album_matches_fragments, matches_found_album = check_album_match(recording, fragments)

    if title_matches_fragments and (matches_found_album + matches_found_artist >= 2):
        logging.warning(
            f"Yaay... artist_matches_fragments: {matches_found_artist} album_matches_fragments: {matches_found_album} title: {title_matches_fragments} {title}")
        return True
    else:
        return False
