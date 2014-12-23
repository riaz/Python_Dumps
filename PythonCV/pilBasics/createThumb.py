#Program to create jpeg thumbnails

import os, sys
from PIL import Image

size = 128,128

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + '.thumb'
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size)
            im.save(outfile,'JPEG')
        except: #Possible conversion errors
            print "Cannot create thumbnail for ", infile
            
