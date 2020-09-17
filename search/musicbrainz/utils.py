def validate_result(result):
    print("now validating")
    score_cache = 0
    recording_to_return = None
    found_valid = True

    for recording in result['recording-list']:
        if int(recording['ext:score']) > score_cache:
            score_cache = int(recording['ext:score'])
            recording_to_return = recording

            if score_cache == 100:
                print("found score 100")
                # check if the artist and album match any entry in fragments
                break

    if score_cache < 90:
        recording_to_return = None
        found_valid = False
        print("score was less than 90")

    if score_cache < 100:
        print(f"settling for less score: {score_cache}")

    return found_valid, recording_to_return
