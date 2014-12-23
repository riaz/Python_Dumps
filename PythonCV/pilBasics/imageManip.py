#Cutting, Pasting and Merging Images

import sys
from PIL import Image

im = Image.open('images/babb.jpg')
box = (10,10,150,150)

region = im.crop(box) #Note: this is a logical region, hence format will be none

#Debugging Line
print region.format , region.size , region.mode

#showing the cropped region
region.show()

#Now, rotating the selected region and pasting it back
region = region.transpose(Image.ROTATE_180)
im.paste(region,box) #Note: here the box refers to zone in im , where to paste region

im.show()


