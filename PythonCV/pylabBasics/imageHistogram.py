#Image Histogram

from PIL import Image
from pylab import *

#reading the image to an array
im = array(Image.open('images/babb.jpg').convert('L'))

#creating a new figure
figure()

#disabling usage of colors
gray()

axis('equal')
axis('off')

#plotting the histogram with pixel frequency counter as bins
hist(im.flatten(),128)
show()
