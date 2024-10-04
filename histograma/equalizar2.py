from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import sys

# Função para normalizar o histograma
def normalizarHistograma(image):
    image_array = np.array(image)
    n_pixels = image_array.shape[0] * image_array.shape[1]
    histograma = np.zeros(256, dtype=np.float32)
    
    for k in np.nditer(image_array):
        histograma[k] += 1
    
    # Normalizando o histograma
    histograma /= n_pixels
    return histograma

# Função para calcular probabilidades acumuladas
def probabilidaes_acumuladas(histogramaNormalizado):
    probabilidades_acumuladas = np.zeros(256, dtype=np.float32)
    probabilidades_acumuladas[0] = histogramaNormalizado[0]

    for i in range(1, len(histogramaNormalizado)):
        probabilidades_acumuladas[i] = histogramaNormalizado[i] + probabilidades_acumuladas[i - 1]
    
    return probabilidades_acumuladas

# Plotando o histograma normalizado
def plot_histograma(histograma, title):
    plt.figure()
    plt.bar(range(256), histograma, width=1)
    plt.title(title)
    plt.xlabel('Intensidade')
    plt.ylabel('Frequência')
    plt.show()

# Função principal
if __name__ == "__main__":
    # Carregar a imagem
    imagem = Image.open(sys.argv[1])
    imagem.show()

    # Normalizar histograma da imagem original
    histograma_normalizado = normalizarHistograma(imagem)
    
    # Plotar o histograma normalizado da imagem original
    plot_histograma(histograma_normalizado, 'Histograma Normalizado da Imagem Original')

    # Calcular as probabilidades acumuladas
    probabilidades = probabilidaes_acumuladas(histograma_normalizado)

    # Criar a lookup table para equalização
    lookup = [round(x * (256 - 1)) for x in probabilidades]

    # Aplicar a equalização na imagem
    imagem_equalizada = imagem.point(lookup)
    imagem_equalizada.show()

    # Normalizar o histograma da imagem equalizada
    histograma_equalizado = normalizarHistograma(imagem_equalizada)
    
    # Plotar o histograma da imagem equalizada
    plot_histograma(histograma_equalizado, 'Histograma da Imagem Equalizada')
