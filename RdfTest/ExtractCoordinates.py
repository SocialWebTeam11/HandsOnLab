__author__ = 'marc'

# -*- coding: utf-8 -*-

import sys
import requests
from BeautifulSoup import BeautifulSoup
from pykml.factory import KML_ElementMaker as KML
from lxml import etree

# This script requires you to add a url of a page with geotags to the commandline, e.g.
# python geo.py 'http://en.wikipedia.org/wiki/Amsterdam'
#URL = sys.argv[1]
URL = 'http://en.wikipedia.org/wiki/Amsterdam'
req = requests.get(URL, headers={'User-Agent' : "Social Web Course Student"})
soup = BeautifulSoup(req.text)

geoTag = soup.find(True, 'geo')

if geoTag and len(geoTag) > 1:
        lat = geoTag.find(True, 'latitude').string
        lon = geoTag.find(True, 'longitude').string
        print 'Location is at', lat, lon
elif geoTag and len(geoTag) == 1:
        (lat, lon) = geoTag.string.split(';')
        (lat, lon) = (lat.strip(), lon.strip())
        print 'Location is at', lat, lon
else:
        print 'No location found'

pml = KML.Placemark(
    KML.name("Amsterdam"),
    KML.Point(
        KML.coordinates("%s,%s" % (lat, lon))
    )
)

file = open("amsterdam.kml", "w")
file.write(etree.tostring(pml))
file.close()

print etree.tostring(pml, pretty_print=True)
