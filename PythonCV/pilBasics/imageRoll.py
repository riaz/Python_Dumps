#Roling an Image

from PIL import Image

#Module is to roll an image sideways
def roll(image,delta):
    xsize,ysize = image.size

    delta = delta * xsize
    if delta == 0: return image

    part1 = image.crop((0,0,delta,ysize))
    part2 = image.crop((delta,0,xsize,ysize))
    image.paste(part2,(0,0,xsize-delta, ysize))
    image.paste(part1, (xsize - delta,0,xsize,ysize))

    return image

im = Image.open('images/babb.jpg')
roll(im,1).show()

