#Using Image Enhancements
#Included methods and modules to enhance images
#Using ImageFilter

from PIL import Image,ImageFilter

im = Image.open('images/babb.jpg')
out = im.filter(ImageFilter.DETAIL)

#Applying point transformations

out = im.point(lambda i: i * 1.2)

out.show() #Output after applying the output filter


