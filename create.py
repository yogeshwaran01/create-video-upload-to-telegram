import argparse
import random

from src.images import peakpx, melody_wallpapers
from src.audio import Genre, download_mp3
from src.utils import save_images, clean
from src.editor import concat_images_in_pictures_dir_to_video, add_output_mp3_audio_to_output_old_mp4

tags = ['vijay', "ajith", "surya", "rajini","kamal", "simbu", "sivakarthikeyan"]

def download_required_images_and_audio(query):
    if query == "m":
        image = peakpx('quotes')[random.randint(0, 38)]
        save_images([image], "pictures")
        download_mp3(Genre.motivation, random.randint(0, 70))
    elif query == "a":
        image = melody_wallpapers()[random.randint(0, 60)]
        save_images([image], "pictures")
        download_mp3(Genre.melody, random.randint(0,  99))
    else:
        image = peakpx(query)[random.randint(0, 38)]
        save_images([image], "pictures")
        download_mp3(Genre.mass, random.randint(0, 30))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--video",
        type=str,
        required=False,
        default="a"
    )
    args = parser.parse_args()
    print("Downloading required images and audio files ...")
    download_required_images_and_audio(args.video)
    print("Converting images into videos ...")
    concat_images_in_pictures_dir_to_video()
    print("Adding audio to the video ...")
    add_output_mp3_audio_to_output_old_mp4()
    print("Cleaning unwanted files ...")
    clean()
