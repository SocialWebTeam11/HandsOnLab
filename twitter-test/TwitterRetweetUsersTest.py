__author__ = 'marc'

import twitter  # Tell Python to use the twitter package

lines = [line.strip() for line in open('twitter.cfg')]

CONSUMER_KEY        = lines[0]
CONSUMER_SECRET     = lines[1]
OAUTH_TOKEN         = lines[2]
OAUTH_TOKEN_SECRET  = lines[3]

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)

q = '#jesuischarlie'  # XXX: Set this variable to a trending topic, or anything else you like.
count = 100  # number of results to retrieve

# See https://dev.twitter.com/docs/api/1.1/get/search/tweets for more info
search_results = twitter_api.search.tweets(q=q, count=count)  # search for your query 'q' 100 times
statuses = search_results['statuses']  # extract the tweets found

# Get the original tweet id for a tweet from its retweeted_status node and insert it here
_retweets = twitter_api.statuses.retweets(id=488100676069646336)

print [
    r['user']['screen_name']
    for r in _retweets
]
