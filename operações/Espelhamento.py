import numpy as np
from PIL import Image
import os


def espelhamento_horizontal(image_path, output_path):

    image = Image.open(image_path)

    w, h = image.size

    img_array = np.array(image)

    # Cria uma nova matriz para a imagem espelhada horizontalmente
    mirrored_img = np.zeros_like(img_array)

    # Preenche a nova imagem espelhada
    for x in range(w):
        for y in range(h):
            new_x = w - 1 - x  # Inverte as colunas (espelhamento horizontal)
            mirrored_img[y, new_x] = img_array[y, x]

    # Converte de volta para uma imagem PIL
    mirrored_image = Image.fromarray(mirrored_img)

    mirrored_image.save(output_path)
    print(f"A imagem espelhada foi salva em: {output_path}")


input_dir = "imagens"
output_dir = "resultados"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

image_path = os.path.join(input_dir, "torre1.png")
output_path = os.path.join(output_dir, "imagem_espelhada_horizontal.jpg")

espelhamento_horizontal(image_path, output_path)
