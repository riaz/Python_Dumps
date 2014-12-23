#Image Contours

from PIL import Image
from pylab import *

#reading the image to an array
im = array(Image.open('images/babb.jpg').convert('L'))

#creating a new figure
figure()

#disabling usage of colors
gray()

#showing contours with origin as upper-left corner
contour(im,origin='image')

axis('equal')
axis('off')

show()
