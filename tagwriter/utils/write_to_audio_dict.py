def write(audio, music_file):
    audio["title"] = music_file.title
    audio["albumartist"] = music_file.album_artist
    audio["artist"] = music_file.contributing_artists
    audio["album"] = music_file.album
    audio["tracknumber"] = music_file.tracknumber
    audio["genre"] = music_file.tags
    audio["date"] = music_file.release_date
    audio["musicbrainz_trackid"] = music_file.musicbrainz_id

    audio.save()
