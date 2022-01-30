from enum import Enum
from pytube import Playlist


class Genre(Enum):
    mass = 1
    melody = 2
    motivation = 3

def download_mp3(type: Genre, id: int):

    if type == Genre.mass:
        target_playlist = "https://www.youtube.com/playlist?list=PLEKi9mUZSLEpQbt5n4PMKArkDd5A1S1aI"
    elif type == Genre.melody:
        target_playlist = "https://www.youtube.com/playlist?list=PLti4gdOly2nnCRZEibywyX9CoTiN2IZ5s"
    elif type == Genre.motivation:
        target_playlist = "https://www.youtube.com/playlist?list=PLhNuphmQyvmY3lssNgplCOgRzZjpQ4blY"
    else:
        target_playlist = "https://www.youtube.com/playlist?list=PLhNuphmQyvmY3lssNgplCOgRzZjpQ4blY"

    p = Playlist(target_playlist)
    required_video = p.videos[id]
    required_video.streams.filter(only_audio=True).first().download(filename=f"output.mp3")
