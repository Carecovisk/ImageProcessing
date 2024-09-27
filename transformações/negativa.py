from PIL import Image
import numpy as np
import sys


def negativa(image):
    image_array = np.array(image)
    height, width, bands = image_array.shape[:3]
    lookup = np.empty(256, dtype=np.uint8)
    for i in range(256):
        lookup[i] = 255 - i

    for i in range(height):
        for j in range(width):
            for k in range(bands):
                image_array[i, j, k] = lookup[image_array[i, j, k]]

    return Image.fromarray(image_array)


img_path = sys.argv[1]
img = Image.open(img_path)

negative_img = negativa(img)
negative_img.show()