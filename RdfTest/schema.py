__author__ = 'marc'

# -*- coding: utf-8 -*-

#import sys
import rdflib
#import rdflib_microdata

# Pass in a URL containing Schema.org microformats
# http://www.last.fm/music/Red+Hot+Chili+Peppers?ac=red
#url = sys.argv[1]

url = "http://www.last.fm/music/Red+Hot+Chili+Peppers?ac=red"

g = rdflib.Graph()
g.parse(url, format="microdata")
print g.serialize()
