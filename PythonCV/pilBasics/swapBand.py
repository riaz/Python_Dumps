#Program to split and merge bands

from PIL import Image

im = Image.open('images/babb.jpg')

r,g,b = im.split()

#Individually managing the color bands in the image
im = Image.merge("RGB", (b,g,r))

im.show()
