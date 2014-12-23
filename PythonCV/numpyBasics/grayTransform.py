#Graylevel Transformations

from PIL import Image
from numpy import *
from pylab import *

#Function: Image Resizing
def imresize(im,sz):
    """ Resize an image array using PIL """

    pil_im = Image.fromarray(im)
    return array(pil_im.resize(sz))


im = array(Image.open('images/babb.jpg').convert('L'))

#Note: Use Image.fromarray(im).convert('RGB') to reverse the above effect

im2 = 255 - im  # This will be an invert image

im3 = (100.0/255) * im + 100 #clamp to interval 100 - 200

im4 = 255.0 * (im / 255.0) ** 2 #squared

#Plotting the invert image
imshow(im4)

#Printing the maximum and minimium value of each image
print int(im4.min()) , int(im4.max())

#Displaying the plot
show()

pil_im = Image.fromarray(imresize(im,(100,200)))
pil_im.convert('RGB')
pil_im.show()





