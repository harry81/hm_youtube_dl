#!/usr/bin/env python

"""
"""

import os, sys
import getopt


def main():
    # options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:g", ["help","go"])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)

    for o, a in opts:
        if o in ("-h", "--help"):
            print __doc__
            sys.exit(0)

        elif o in ("-g", "--go"):
            address = args[0]

        else:
            print 'else'

        filename = getFilename(address).rstrip()
#        filename = filename.replace(' ','')
#        downFile(address, filename)
        savaAsmp4(filename)
        

def getFilename(addr):
    print "Geting a file name ......."
    cmd = "youtube-dl --get-filename  -o '%(title)s-%(uploader)s.%(ext)s'  "
    cmd = cmd + addr
    rlt = os.popen(cmd,'r')
    text = rlt.read()

    return text

def downFile(addr, filename):
    print "Downloading a file ......."
    cmd = "youtube-dl  -o '%(title)s-%(uploader)s.%(ext)s'  "
    cmd = cmd + addr
    print cmd
    
    rlt = os.popen(cmd,'r')
    text = rlt.read()

    return text

def savaAsmp4(filename):
    print "Saveing ......."
    src = filename.rstrip()
    filename = filename.replace(' ','')
    dst = os.path.splitext(filename)[0] + '.mp4'
    cmd = "ffmpeg -i \'%s\' -f avi -vcodec mpeg4 -b 800 \'%s\' " % (src, dst)
    rlt = os.popen(cmd,'r')
    text = rlt.read()

    print cmd

    

if __name__ == "__main__":
    main()

# youtube-dl --get-filename  -o '%(title)s-%(uploader)s.%(ext)s'  'http://www.youtube.com/watch?feature=player_detailpage&v=YKV3rhzvaC8'

# youtube-dl -o '%(title)s-%(uploader)s.%(ext)s'  'http://www.youtube.com/watch?feature=player_detailpage&v=YKV3rhzvaC8'

# ffmpeg -i MoldytoasterMedia3.flv -f avi -vcodec mpeg4 -b 800 o.avi
