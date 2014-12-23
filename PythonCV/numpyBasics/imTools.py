import numpy
""" Function: Image Resizing
    Description: Function resizes and numpy image array to the size provided
    Parameters:
                im - numpy image array
                sz - resize size eg: (200,300)
    Return:
            Resized Numpy array                    
"""

def imresize(im,sz):
    pil_im = Image.fromarray(im)
    return array(pil_im.resize(sz))


"""
    Function    : Histogram Equalization
    Description : Flattens the graylevel histogram of an image, so that all intensities are as equal as possible,
                  This function is used to normalize image intensity, and computes the histogram equalization of a
                  grayscale image
                  
    Parameters   :
                    im       - numpy image array
                    nvr_bins - histogram bin count
    Return:
            Equalized image histogram along with cdf
    
"""

def histeq(im,nbr_bins=256):
    #get image histogram
    imhist,bins = histogram(im.flatten(),nbr_bins,normed=True)

    #applying cumulative distribution function
    cdf = imhist.cumsum()
    cdf = 255 * cdf[-1] #normalize

    #using linear interpolation to cdf to find new pixel values
    im2 = interp(im.flatten(),bins[:-1],cdf)

    return im2.reshape(im.shape) , cdf
        
