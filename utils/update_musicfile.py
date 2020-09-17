from utils.result_parser import parse_musicbrainz_result


def update_musicfile(musicfile, recording):
    parsed_results = parse_musicbrainz_result(recording)

    musicfile.title = parsed_results['title']
    musicfile.album = parsed_results['album']
    musicfile.album_artist = parsed_results['album_artist']
    musicfile.contributing_artists = parsed_results['contributing_artists']
    musicfile.release_date = parsed_results['release_date']
    musicfile.tracknumber = parsed_results['tracknumber']
    musicfile.tags = parsed_results['tags']
    musicfile.length = parsed_results['length']
