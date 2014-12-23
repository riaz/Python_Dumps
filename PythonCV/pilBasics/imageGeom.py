#Geometrical Transformations

from PIL import Image

#Using methods resize,rotate  and transpose of the Image class

im = Image.open('images/babb.jpg')
out = im.resize((128,128))
out = im.rotate(90) #rotating 45 degrees clock-wise
#or use -> out = im.transpose(Image.ROTATE_90)
out.show()

