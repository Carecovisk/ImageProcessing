from PIL import Image
import sys, os
import numpy as np

def reducao_bilinear(original_image: Image) -> Image:
    array_original_image = np.array(original_image, dtype=np.int32)
    print(f"Resolução antes: {array_original_image.shape[0]}X{array_original_image.shape[1]}")
    original_image.show()
    height, width, bands = array_original_image.shape[:3]

    new_height = int(height / 2)
    new_width = int(width / 2)
    
    array_new_image = np.zeros((new_height, new_width, bands), dtype=np.uint8)

    for i in range(new_height):
        for j in range(new_width):
            pixel_sum = array_original_image[2 * i, 2 * j]
            pixel_sum += array_original_image[2 * i + 1, 2 * j]
            pixel_sum += array_original_image[2 * i, 2 * j + 1]
            pixel_sum += array_original_image[2 * i + 1, 2 * j + 1]
            
            array_new_image[i, j] = pixel_sum / 4
    
    print(f"Resolução depois: {array_new_image.shape[0]}X{array_new_image.shape[1]}")
    new_image = Image.fromarray(array_new_image)
    return new_image

try:
    image_path, times = sys.argv[1:]
    img = Image.open(image_path)
    for i in range(int(times)):
        img = reducao_bilinear(img)
    img.show()
except IndexError:
    print(f"Uso correto: python {os.path.basename(__file__)} <caminho_para_imagem> <numero_de_reduções>")