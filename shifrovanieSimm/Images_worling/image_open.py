from PIL import Image
import numpy as np

def search_max_delitel(n: int):
    for i in range(n // 2, 0, -1):
        if n % i == 0:
            return i


img = Image.open('new.png')
size = img.size

pixels = []
for i in np.array(img):
    a = []
    for j in i:
        b = []
        for l in j:
            b.append(255 - l)
        a.append(tuple(b))
    pixels.append(a)
pixels = np.array(pixels, dtype=np.uint8)
nem = Image.fromarray(pixels).save('123456789.png')
# for i in range(size[0]):
#     a = []
#     for j in range(size[1]):
#         a.append(img.getpixel((i, j)))
#     print(a)