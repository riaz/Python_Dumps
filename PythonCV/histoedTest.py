#Image Histogram Equalization test

from PIL import Image
from pylab import *
#import api
import numpy

def histeq(im,nbr_bins=256):
    #get image histogram
    imhist,bins = histogram(im.flatten(),nbr_bins,normed=True)

    #applying cumulative distribution function
    cdf = imhist.cumsum()
    cdf = 255 * cdf[-1] #normalize

    #using linear interpolation to cdf to find new pixel values
    im2 = interp(im.flatten(),bins[:-1],cdf)

    return im2.reshape(im.shape) , cdf
        

im = array(Image.open('numpyBasics/images/babb.jpg').convert('L'))
im2,cdf = histeq(im)

im2.show()

