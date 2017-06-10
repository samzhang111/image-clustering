import sys

from PIL import Image

image = Image.open(sys.argv[1])

image.convert("L")
