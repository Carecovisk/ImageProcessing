from PIL import Image
from random import randint
import sys, time
import numpy as np

def image_subtract(Image1, Image2):
    img1 = np.array(Image1)
    img2 = np.array(Image2)
    return Image.fromarray(img1 - img2)

img1_path, img2_path = sys.argv[1:]
img1 = Image.open(img1_path)
img2 = Image.open(img2_path)
# Subtração
diference = image_subtract(img1, img2)

img1.show('Image1')
time.sleep(1)
img2.show('Image2')
time.sleep(1)
diference.show('Diferença')