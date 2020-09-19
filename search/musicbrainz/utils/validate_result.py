import logging

from search.musicbrainz.utils.check_match import check_title_match


def validate_result(result, fragment, fragments):
    print("now validating")
    score_cache = 0
    matches_cache = 0
    recording_to_return = None
    found_valid = True

    try:
        for recording in result['recording-list']:
            title = recording["title"].lower()
            recording_score = int(recording['ext:score'])

            if title in fragments or check_title_match(title, fragments, threshold=3):
                if recording_score >= score_cache:
                    score_cache = recording_score
                    recording_to_return = recording

                    if score_cache == 100:
                        print("found score 100")
                        break
            else:
                logging.warning(f"Couldn't validate title {title} against fragments. Skipping to next iteration")
                continue

    except KeyError as key_error:
        logging.warning(f"Key {key_error.args} not found.Validation failed  so move on to next iteration.")

    if score_cache < 90:
        recording_to_return = None
        found_valid = False
        logging.warning("Score after iterations was less than 90.Cant return this as valid result. Bailing...")
    elif 90 <= score_cache < 100:
        logging.warning(f"settling for less score: {score_cache}")

    return found_valid, recording_to_return
