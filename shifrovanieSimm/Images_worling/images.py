from PIL import Image
import numpy as np
from random import randint


# заявление об отсутствии
def random_image(width: int, height: int, save_as: str, frm: int = 0, to: int = 256):
    pixels = [
        [list(randint(frm, to) for _ in range(3)) for _ in range(width)] for _ in range(height)
    ]
    # Convert the pixels into an array using numpy
    array = np.array(pixels, dtype=np.uint8)

    # Use PIL to create an image from the new array of pixels
    image = Image.fromarray(array)
    image.show()
    image.save(save_as)


def new_image(pixels: list, save_as: str):
    # Convert the pixels into an array using numpy
    array = np.array(pixels, dtype=np.uint8)

    # Use PIL to create an image from the new array of pixels
    new_image = Image.fromarray(array)
    new_image.save(save_as)


def inverse(path: str, save_as: str):
    img = np.array(Image.open(path))
    pixels = []
    for i in img:
        a = []
        for j in i:
            b = []
            for l in j:
                b += [255 - l]
            a.append(tuple(b))
        pixels.append(a)
    pixels = np.array(pixels, dtype=np.uint8)
    image = Image.fromarray(pixels)
    image.save(save_as)


def encode_photo(path: str, save_as: str):
    key = '1234567891'
    img = np.array(Image.open(path))
    pixels = []
    q = 0
    for i in img:
        a = []
        for j in i:
            b = []
            for l in j:
                b.append(l // int(key[q % len(key)]))
                q += 1
            a.append(tuple(b))
        pixels.append(a)
    pixels = np.array(pixels, dtype=np.uint8)
    image = Image.fromarray(pixels)
    image.save(save_as)


def decode_photo(path: str, save_as: str):
    key = '1234567891'
    img = np.array(Image.open(path))
    pixels = []
    q = 0
    for i in img:
        a = []
        for j in i:
            b = []
            for l in j:
                b.append(l * int(key[q % len(key)]))
                q += 1
            a.append(tuple(b))
        pixels.append(a)
    pixels = np.array(pixels, dtype=np.uint8)
    image = Image.fromarray(pixels)
    image.save(save_as)


decode_photo('photos.png', 'photoss.png')