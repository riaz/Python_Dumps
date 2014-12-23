from PIL import Image

#convert an image to 3 types
# 1. RGB  2.L or grayscale 3. CMYK
pil_im = Image.open('images/babb.jpg').convert('RGB')
print pil_im.format , pil_im.size , pil_im.mode

#showing the image just loaded
pil_im.show()
