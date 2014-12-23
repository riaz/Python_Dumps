#Image plot with interactive annotations

from PIL import Image
from pylab import *

im = array(Image.open('images/babb.jpg'))
imshow(im) #Plotting the image array in the figure

print 'Please click 3 points'
x = ginput(3)
print 'you clicked: ' , x
show()

