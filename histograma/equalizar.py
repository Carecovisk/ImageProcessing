from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import sys


def normalizarHistograma(image):
    image_array = np.array(image)
    n_pixels = image_array.shape[0] * image_array.shape[1]
    histograma = np.zeros(256, dtype=np.float32)
    print(image_array.shape)
    for k in np.nditer(image_array):
        histograma[k] += 1
    
    for k in range(histograma.__len__()):
        histograma[k] /=  n_pixels
    return histograma


def probabilidaes_acumuladas(histogramaNormalizado):
    probabilidades_acumuladas = np.zeros(256, dtype=np.float32)
    probabilidades_acumuladas[0] = histogramaNormalizado[0]


    for i in range(1, histogramaNormalizado.__len__()):
        probabilidades_acumuladas[i] = histogramaNormalizado[i] + probabilidades_acumuladas[i - 1]
    
    return probabilidades_acumuladas

imagem = Image.open(sys.argv[1])
imagem.show()
histograma_normalizado = normalizarHistograma(imagem)

probabilidades = probabilidaes_acumuladas(histograma_normalizado)
# Criando Lookup table
lookup = [round(x * (256 - 1)) for x in probabilidades]
imagem_equalizada = imagem.point(lookup)
imagem_equalizada.show()