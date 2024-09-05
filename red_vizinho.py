from PIL import Image
import numpy as np


def reducao_vizinho_mais_proximo(img_path, output_path, new_size):
    print(f"Abrindo imagem de: {img_path}")
    image = Image.open(img_path)
    original_width, original_height = image.size
    print(f"Dimensões da imagem original: {original_width}x{original_height}")

    image_array = np.array(image)
    new_width, new_height = new_size
    print(f"Redimensionando para: {new_width}x{new_height}")

    resized_array = np.zeros(
        (new_height, new_width, image_array.shape[2]), dtype=image_array.dtype)
    x_scale = original_width / new_width
    y_scale = original_height / new_height

    for y in range(new_height):
        for x in range(new_width):
            orig_x = int(x * x_scale)
            orig_y = int(y * y_scale)
            resized_array[y, x] = image_array[orig_y, orig_x]

    resized_image = Image.fromarray(resized_array)
    print(f"Salvando imagem redimensionada em: {output_path}")
    resized_image.save(output_path)


input_img_path = 'imagens/casa.png'
output_img_path = 'Resultados/casa_redimensionado.png'
new_size = (100, 100)

reducao_vizinho_mais_proximo(input_img_path, output_img_path, new_size)
