__author__ = 'marc'

import facebook
import json
# A helper function to pretty-print Python objects as JSON
def pp(o):
    print json.dumps(o, indent=1)

lines = [line.strip() for line in open('facebook.cfg')]

token = lines[0]

# Create a connection to the Graph API with your access token
g = facebook.GraphAPI(token)

# Execute a few sample queries
print '---------------'
print 'Me'
print '---------------'
pp(g.get_object('me'))
print
print '---------------'
print 'My Friends'
print '---------------'
pp(g.get_connections('me', 'friends'))
print
print '---------------'
print 'Pages about UVA'
print '---------------'
pp(g.request('search', {'q': 'Universiteit van Amsterdam', 'type': 'page', 'limit': 5}))
print
print '---------------'
print 'Pages about VU'
print '---------------'
pp(g.request('search', {'q': 'Vrije Universiteit Amsterdam', 'type': 'page', 'limit': 5}))

# Use the ids to query for likes
uva_id = '313972021952684'
vu_id = '116356121481'

# A quick way to format integers with commas every 3 digits
def int_format(n): return "{:,}".format(n)

print "UVA likes:", int_format(g.get_object(uva_id)['likes'])
print "VU likes:", int_format(g.get_object(vu_id)['likes'])