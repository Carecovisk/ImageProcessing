from PIL import Image
import numpy as np
import sys

def filtro_da_media(image : Image.Image) -> Image.Image:
    image = image.convert('HSV')
    image_array = np.asarray(image)
    height, width, bands = image_array.shape
    mascara = np.ones((3, 3))
    new_image_array = np.copy(image_array)

    for i in range(1, height -1):
        for j in range(1, width - 1):
            sum = np.zeros(3, dtype=np.float16)

            index_y = 0
            for k in range(i -1, i + 2):
                index_x = 0
                for l in range(j - 1, j + 2):
                    sum += mascara[index_y][index_x] * image_array[k][l]
                    index_x += 1
                index_y += 1
            
            new_image_array[i][j] = sum / 9
    
    return Image.fromarray(new_image_array, mode='HSV')


image_path = sys.argv[1]
image = Image.open(image_path)
image.show()
result_image = filtro_da_media(image)
result_image.show()