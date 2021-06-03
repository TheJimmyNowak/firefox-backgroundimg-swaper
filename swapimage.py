import os
import random

def get_files(path: str) -> list:
    assert path is not None

    return [f for f in os.listdir(path)]

def rename() -> None:
    img = random.choice(get_files('img/'))

    if img == "1.jpg":
        return

    os.rename("img/1.jpg", "img/" + str(random.randint(1, 99999999999))+ ".jpg")
    os.rename("img/" + img, "img/1.jpg")

rename()
