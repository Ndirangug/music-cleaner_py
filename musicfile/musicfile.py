from _datetime import datetime, timezone

from tagwriter import mp3_writer, ogg_writer
from utils.audio_format import *
from utils.filename_splitter import get_file_name

EPOCH = datetime(1970, 1, 1, tzinfo=timezone.utc)


class MusicFile:
    def __init__(self, file_path: str, audioformat: AudioFormat, title="", album="", album_artist="",
                 contributing_artists=list(), artist_credit_phrase="", tags=[], release_date=EPOCH, musicbrainz_id="",
                 length="", tracknumber=0):
        self.file_path = file_path
        self.audioformat = audioformat
        self.title = title
        self.album = album
        self.album_artist = album_artist
        self.contributing_artists = contributing_artists
        self.artist_credit_phrase = artist_credit_phrase
        self.tags = tags
        self.release_date = release_date
        self.musicbrainz_id = musicbrainz_id
        self.length = length
        self.tracknumber = tracknumber

    def save_to_disk(self):
        new_filename = f'{self.tracknumber} {self.title} -  {self.artist_credit_phrase} - {self.album}'.strip()
        old_filename = get_file_name(self.file_path)

        new_path = self.file_path.replace(old_filename, new_filename)
        print('saving to disk.. ' + new_path)

        if self.audioformat == AudioFormat.MP3:
            mp3_writer.write_to_file(music_file=self)
        elif self.audioformat == AudioFormat.OGGVORBIS or self.audioformat == AudioFormat.OGGOPUS:
            ogg_writer.write_to_file(music_file=self)
