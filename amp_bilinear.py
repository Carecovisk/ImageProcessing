from PIL import Image
import numpy as np


def ampliacao_bilinear(img_path, output_path, new_size):
    image = Image.open(img_path)
    original_width, original_height = image.size

    image_array = np.array(image)

    new_width, new_height = new_size

    resized_array = np.zeros(
        (new_height, new_width, image_array.shape[2]), dtype=np.uint8)

    x_scale = (original_width - 1) / (new_width - 1)
    y_scale = (original_height - 1) / (new_height - 1)

    for y in range(new_height):
        for x in range(new_width):
            orig_x = x * x_scale
            orig_y = y * y_scale

            x1 = int(orig_x)
            x2 = min(x1 + 1, original_width - 1)
            y1 = int(orig_y)
            y2 = min(y1 + 1, original_height - 1)

            x_frac = orig_x - x1
            y_frac = orig_y - y1

            for c in range(image_array.shape[2]):
                top = (1 - x_frac) * \
                    image_array[y1, x1, c] + x_frac * image_array[y1, x2, c]
                bottom = (1 - x_frac) * \
                    image_array[y2, x1, c] + x_frac * image_array[y2, x2, c]
                resized_array[y, x, c] = int(
                    (1 - y_frac) * top + y_frac * bottom)

    resized_image = Image.fromarray(resized_array)

    resized_image.save(output_path)


input_img_path = 'imagens/casa.png'
output_img_path = 'Resultados/casa_ampliada_bilinear.png'
new_size = (600, 600)

ampliacao_bilinear(input_img_path, output_img_path, new_size)
