from PIL import Image
from random import randint
import sys, time
import numpy as np

def image_subtract(Image1, Image2):
    img1 = np.array(Image1)
    img2 = np.array(Image2)
    return Image.fromarray(img1 - img2)

img_path = sys.argv[1]
img = Image.open(img_path)
# Zera aleatoriamente valores da imagem
modified_img = img.point(lambda i : 0 if randint(1, 100) <= 10 else i)
# Subtração
diference = image_subtract(img, modified_img)

img.show('Original')
time.sleep(1)
modified_img.show('Modificada')
time.sleep(1)
diference.show('Diferença')