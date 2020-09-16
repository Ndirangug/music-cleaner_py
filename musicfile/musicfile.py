from _datetime import datetime, timezone
from utils.audio_format import *

EPOCH = datetime(1970, 1, 1, tzinfo=timezone.utc)


class MusicFile:
    def __init__(self, file_path: str, audioformat: AudioFormat, title="", album="", album_artist="",
                 contributing_artists=list(), genre="", release_date=EPOCH, musicbrainz_id=""):
        self.file_path = file_path
        self.audioformat = audioformat
        self.title = title
        self.album = album
        self.album_artist = album_artist
        self.contributing_artists = contributing_artists
        self.genre = genre
        self.release_date = release_date
        self.musicbrainz_id = musicbrainz_id

    def save_to_disk(self):
        # TODO Save tags
        pass
