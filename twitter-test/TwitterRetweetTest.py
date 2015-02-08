__author__ = 'marc'

import twitter  # Tell Python to use the twitter package
from prettytable import PrettyTable

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

retweets = [
    (
        status['retweet_count'],
        status['retweeted_status']['user']['screen_name'],
        status['text']
    )  # Store out a tuple of these three values
    for status in statuses  # for each status
        if status.has_key('retweeted_status')  # ... so long as the status meets this condition.
]

# Slice off the first 5 from the sorted results and display each item in the tuple
pt = PrettyTable(field_names=['Count', 'Screen Name', 'Text'])
[
    pt.add_row(row)
    for row in sorted(retweets, reverse=True)[:5]
]
pt.max_width['Text'] = 50
pt.align = 'l'

print pt
