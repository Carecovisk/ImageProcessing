from PIL import Image
import sys

image_path = sys.argv[1]
image = Image.open(image_path)
print(image.getbands())
image.show()