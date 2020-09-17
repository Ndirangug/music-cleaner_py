from _datetime import datetime, timezone

from utils.audio_format import *

EPOCH = datetime(1970, 1, 1, tzinfo=timezone.utc)


class MusicFile:
    def __init__(self, file_path: str, audioformat: AudioFormat, title="", album="", album_artist="",
                 contributing_artists=list(), tags=[], release_date=EPOCH, musicbrainz_id="", length="", tracknumber=0):
        self.file_path = file_path
        self.audioformat = audioformat
        self.title = title
        self.album = album
        self.album_artist = album_artist
        self.contributing_artists = contributing_artists
        self.tags = tags
        self.release_date = release_date
        self.musicbrainz_id = musicbrainz_id
        self.length = length
        self.tracknumber = tracknumber

    def save_to_disk(self):
        # TODO Save tags
        pass
