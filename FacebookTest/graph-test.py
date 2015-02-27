__author__ = 'marc'

import networkx as nx
from networkx.readwrite import json_graph
import requests
import facebook
import json

lines = [line.strip() for line in open('facebook.cfg')]
token = lines[0]
g = facebook.GraphAPI(token)

friends = [(friend['id'], friend['name'])
           for friend in g.get_connections('me', 'friends')['data']]

#me = g.get_connections('me')

#print me


#me/?fields=friends{name,picture{url},link,cover,photos,movies{cover},music{cover}}
#url = 'https://graph.facebook.com/%s?fields=name, location, context.fields{mutual_friends}&access_token=%s'

url = 'https://graph.facebook.com/%s?fields=name,location,picture{url},link,cover,photos,movies{cover},music{cover}&access_token=%s'

mutual_friends = {}
photos = {}
movies = {}
pictures = {}
avatars = {}

#links = {friend.get_object('link') for friend in friends}

#print links

# This loop spawns a separate request for each iteration, so
# it may take a while.
for friend_id, friend_name in friends:
    pictureList = []

    r = requests.get(url % (friend_id, token))
    response_data = json.loads(r.content)
    try:
        for cover in response_data['music']['data']:
            pictureList.append(cover['cover']['source'])
    except KeyError:
        pass
    try:
        for cover in response_data['movies']['data']:
            pictureList.append(cover['cover']['source'])
    except KeyError:
        pass
    try:
        for cover in response_data['photos']['data']:
            pictureList.append(cover['cover']['source'])
    except KeyError:
        pass
    #try:
        #pictureList.append(response_data['picture']['data']['url'])
    #except KeyError:
        #pass
    try:
        pictureList.append(response_data['cover']['source'])
    except KeyError:
        pass
    mutual_friends[friend_name] = [pictureList.append(response_data['picture']['data']['url'])]
    pictures[friend_name] = pictureList

#print mutual_friends
for friend_id, friend_name in friends:
    print pictures[friend_name]

nxg = nx.Graph()

#[nxg.add_edge('me', mf) for mf in mutual_friends]

[nxg.add_edge(f1, f2)
 for f1 in mutual_friends
 for f2 in mutual_friends[f1]]

[nxg.add_edge(f1, f2)
 for f1 in mutual_friends
 for f2 in pictures[f1]]

# Serializing a NetworkX graph to a file for consumption by D3
nld = json_graph.node_link_data(nxg)
json.dump(nld, open('viz/force.json', 'w'))