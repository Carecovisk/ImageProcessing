from PIL import Image
import numpy as np
import sys

def filtro_laplaciano(image : Image.Image, mascara) -> Image.Image:
    image = image.convert('HSV')
    image_array = np.asarray(image)
    height, width, bands = image_array.shape[:3]
    mascara = np.array(mascara)
    new_image_array = np.copy(image_array)

    for i in range(1, height -1):
        for j in range(1, width - 1):
            sum = np.zeros(bands, dtype=np.float16)

            index_y = 0
            for k in range(i -1, i + 2):
                index_x = 0
                for l in range(j - 1, j + 2):
                    sum += mascara[index_y][index_x] * image_array[k][l]
                    index_x += 1
                index_y += 1
            
            sum[sum < 0] = 0
            new_image_array[i][j] = sum
    
    return Image.fromarray(new_image_array, mode='HSV').crop((1, 1, width -1, height -1))


mascaras = [
    [
        [0, 1, 0],
        [1, -4, 1],
        [0, 1, 0]
    ],
    [
        [1, 1, 1],
        [1, -8, 1],
        [1, 1, 1]
    ],
    [
        [0, -1, 0],
        [-1, 4, -1],
        [0, -1, 0]
    ],
    [
        [-1, -1, -1],
        [-1, 8, -1],
        [-1, -1, -1]
    ]
]

image_path = sys.argv[1]
image = Image.open(image_path)
image.show()

for mascara in mascaras:
    result_image = filtro_laplaciano(image, mascara)
    result_image.show()