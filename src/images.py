import requests
from bs4 import BeautifulSoup

def peakpx(query: str) -> list[str]:
    markup = requests.get(f"https://www.peakpx.com/en/search?q={query}").text
    soup = BeautifulSoup(markup, "html.parser")
    image_tags = soup.find_all("img", {'class', 'lazy lst_img'})

    return list(map(lambda tag: tag['data-src'], image_tags))

def wallpapercave(folder: str):
    markup = requests.get(f"https://wallpapercave.com/{folder}").text
    soup = BeautifulSoup(markup, "html.parser")
    div_tags = soup.find_all("img", {'class', 'wpimg'})
    images_is = map(lambda tag: "https://wallpapercave.com" + tag.get('src'), div_tags)

    return list(images_is)

def melody_wallpapers():
    p = wallpapercave("tamil-romantic-wallpapers")
    p.extend((wallpapercave("tamil-love-couples-wallpapers")))
    return p
