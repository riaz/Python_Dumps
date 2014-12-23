#Program to convert files to JPEG

import os,sys
from PIL import Image

print sys.argv
for infile in sys.argv[1:]:
    print infile
    f, e    = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print "Cannot Convert", infile
