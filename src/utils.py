import os
import requests
import shutil

def save_images(images: list, directory: str) -> None:
    os.mkdir(directory)
    c = 1
    for image in images:
        res = requests.get(image, stream=True)
        with open(f"./{directory}/{c}.jpeg", "wb") as f:
            res.raw.decode_content = True
            shutil.copyfileobj(res.raw, f)
        c = c + 1



def clean():
    shutil.rmtree("pictures")
    os.system("rm output_old.mp4")
    os.system("rm output.mp3")
