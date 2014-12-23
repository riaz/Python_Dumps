#Plotting images,points and lines

from PIL import Image
from pylab import *

#reading image to array
im = array(Image.open('images/babb.jpg'))

#plotting the image
imshow(im)

#show points
x = [100,100,400,400]
y = [200,500,200,500]

#point the points with red star markers
#Other options:
#1. plot(x,y)       -> default blue solid line
#2. plot(x,y,'go-') -> green line with circle-markers
#3. plot(x,y,'ks:') -> black dotted line with square-markers

plot(x,y,'r*')

#line plot connecting the first two points
plot(x[:2],y[:2])

#adding the title and showing the plot
title('Plotting: "babb.jpg"')

#setting axis off
axis('off')

#rendering
show()



