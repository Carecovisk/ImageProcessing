import numpy as np
from PIL import Image
import os


def sum_images(image1_path, image2_path, output_path):

    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    img_array1 = np.array(image1)
    img_array2 = np.array(image2)

    if img_array1.shape != img_array2.shape:
        raise ValueError(
            "As imagens devem ter o mesmo tamanho para serem somadas.")

    # Soma as imagens pixel a pixel
    summed_img = (img_array1 + img_array2)/2

    summed_image = Image.fromarray(summed_img.astype(np.uint8))

    summed_image.save(output_path)
    print(f"A imagem somada foi salva em: {output_path}")


input_dir = "imagens"
output_dir = "resultados"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

image1_path = os.path.join(input_dir, "paisagem.jpg")
image2_path = os.path.join(input_dir, "textura.jpg")
output_path = os.path.join(output_dir, "imagem_somada.jpg")

sum_images(image1_path, image2_path, output_path)
