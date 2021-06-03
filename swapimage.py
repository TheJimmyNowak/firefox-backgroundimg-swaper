#!/usr/bin/python3
import os
import random
import sys

def get_files(path: str) -> list:
    assert path is not None

    return [f for f in os.listdir(path)]

def rename(path: str) -> None:
    img = random.choice(get_files(path))
    assert get_files(path) != [] 
    print(get_files(path))

    if img == "1.jpg":
        return

    os.rename(path + "1.jpg", path + str(random.randint(1, 99999999999))+ ".jpg")
    os.rename(path + img, path+"/1.jpg")

path = sys.argv[1]
rename(path)
