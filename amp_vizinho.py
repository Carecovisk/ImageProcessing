from PIL import Image
import sys, os
import numpy as np

def ampliacao_vizinho_mais_proximo(img_path: str, escala = 2) -> Image:
    img = Image.open(img_path)
    img.show()
    img_original_array = np.array(img)
    
    print(f"Resolução antes: {img_original_array.shape[0]}X{img_original_array.shape[1]}")

    height, width, bands = img_original_array.shape[:3]

    new_height = height * escala
    new_width = width * escala
    new_img_array = np.zeros((new_height, new_width, bands), dtype=np.uint8)

    for i in range(new_height):
        for j in range(new_width):
            # Calcula qual é a posição do pixel na imagem original que deve ser usada para prencher
            # os novos espaços na nova matriz.
            x_img_original = int(i / escala)
            y_img_original = int(j / escala)
            # Atribui pixel da imagem original na nova imagem
            new_img_array[i, j] = img_original_array[x_img_original, y_img_original]
    
    print(f"Resolução depois: {new_img_array.shape[0]}X{new_img_array.shape[1]}")
    new_img = Image.fromarray(new_img_array)
    return new_img

try:
    image, scale = sys.argv[1:]
    img = ampliacao_vizinho_mais_proximo(image, int(scale))
    img.show()
except ValueError:
    print(f"Uso correto: python {os.path.basename(__file__)} <caminha_para_imagem> <fator_de_escala>")