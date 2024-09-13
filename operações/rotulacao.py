from PIL import Image
import sys
import numpy as np

def rotular(image):
    image_array = np.array(image)
    height, width = image_array.shape[:2]
    labels = []
    equivalent_labels = []
    k = 0
    for i in range(1, height):
        for j in range(1, width):
            pixel = image_array[i, j]
            if pixel == 0:
                continue
            else:
                left_pixel = image_array[i, j - 1]
                top_pixel = image_array[i - 1, j]

                if left_pixel == 0 and top_pixel == 0:
                    labels.append(k * 2)
                    image_array[i, j] -= labels[k] # Marcando pixel
                    k += 1
                elif left_pixel == top_pixel:
                    label = 255 - left_pixel
                    image_array[i, j] -= label
                elif left_pixel != 0 and top_pixel != 0:
                    label_top = 255 - top_pixel
                    label_left = 255 - left_pixel
                    equivalent_labels.append({label_top, label_left})
                    image_array[i, j] -= label_top
                else:
                    label = 255 - top_pixel if left_pixel == 0 else 255 - left_pixel
                    image_array[i, j] -= label
    
    i = 0
    while i < equivalent_labels.__len__() - 1:
        j = i + 1
        while j < equivalent_labels.__len__():
            intersection = equivalent_labels[i].intersection(equivalent_labels[j])
            if len(intersection) > 0:
                equivalent_labels[i] = equivalent_labels[i].union(equivalent_labels[j])
                equivalent_labels.pop(j)
            else:
                j += 1
        i += 1

    for i in range(1, height):
        for j in range(1, width):
            if image_array[i, j] != 0:
                for label_set in equivalent_labels:
                    if 255 - image_array[i, j] in label_set:
                        image_array[i, j] = 255 - min(label_set)
                        break
    
    return Image.fromarray(image_array)



image_path = sys.argv[1]
image = Image.open(image_path)
image.show()
rotular(image).show()