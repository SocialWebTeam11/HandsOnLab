__author__ = 'marc'

import twitter  # Tell Python to use the twitter package
from collections import Counter
import matplotlib.pyplot as plt

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

status_texts = [
    status['text']
    for status in statuses
]

# Compute a collection of all words from all tweets
words = [w for t in status_texts for w in t.split()]  # split the string on the empty spaces

word_counts = sorted(Counter(words).values(), reverse=True)

plt.loglog(word_counts)
plt.ylabel("Freq")
plt.xlabel("Word Rank")
plt.show()