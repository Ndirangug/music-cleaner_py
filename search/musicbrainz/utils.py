import logging


def validate_result(result, fragment, fragments):
    print("now validating")
    score_cache = 0
    recording_to_return = None
    found_valid = True

    title = ""
    artist = ""
    album = ""

    for recording in result['recording-list']:
        if int(recording['ext:score']) > score_cache:
            score_cache = int(recording['ext:score'])
            recording_to_return = recording

            title = recording["title"].lower()
            artist = recording["artist-credit"][0]["artist"]["name"].lower()
            album = recording['release-list'][0]['title'].lower()

            if score_cache == 100:
                print("found score 100")
                # TODO check if the artist and album match any entry in fragments
                if title in fragments:
                    break

    if score_cache < 90:
        recording_to_return = None
        found_valid = False
        logging.warning("score was less than 90")

    if title in fragments:
        pass
    else:
        recording_to_return = None
        found_valid = False
        logging.warning(f"Could not find the the returned title, album or artist in the filename fragmments and so "
                        f"cannot validate this result though score is {score_cache} \n Fragment: {fragment} \n"
                        f" Result: title: {title} artist: {artist} album:{album}")

    if score_cache < 100:
        logging.warning(f"settling for less score: {score_cache}")

    return found_valid, recording_to_return
