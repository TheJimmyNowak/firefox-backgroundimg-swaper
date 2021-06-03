import os
import random
import sys

path = sys.argv[1]

def get_files(path: str) -> list:
    assert path is not None

    return [f for f in os.listdir(path)]

def rename(path: str) -> None:
    img = random.choice(get_files('img/'))

    if img == "1.jpg":
        return

    os.rename("img/1.jpg", "img/" + str(random.randint(1, 99999999999))+ ".jpg")
    os.rename("img/" + img, "img/1.jpg")

rename(path)
