__author__ = 'marc'

import twitter  # Tell Python to use the twitter package
import json

lines = [line.strip() for line in open('twitter.cfg')]

CONSUMER_KEY        = lines[0]
CONSUMER_SECRET     = lines[1]
OAUTH_TOKEN         = lines[2]
OAUTH_TOKEN_SECRET  = lines[3]

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)

WORLD_WOE_ID = 727232  # The Yahoo! Where On Earth ID for the entire world
world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)  # get back a callable
# print world_trends

print json.dumps(world_trends[0], indent=2)