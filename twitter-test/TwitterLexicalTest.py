__author__ = 'marc'

import twitter  # Tell Python to use the twitter package

lines = [line.strip() for line in open('twitter.cfg')]

CONSUMER_KEY = lines[0]
CONSUMER_SECRET = lines[1]
OAUTH_TOKEN = lines[2]
OAUTH_TOKEN_SECRET = lines[3]

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)

q = '#jesuischarlie'  # XXX: Set this variable to a trending topic, or anything else you like.
count = 100  # number of results to retrieve

# See https://dev.twitter.com/docs/api/1.1/get/search/tweets for more info
search_results = twitter_api.search.tweets(q=q, count=count)  # search for your query 'q' 100 times
statuses = search_results['statuses']  # extract the tweets found

status_texts = [
    status['text'] for status in statuses]

screen_names = [
    user_mention['screen_name']
    for status in statuses
    for user_mention in status['entities']['user_mentions']
]

hashtags = [
    hashtag['text']
    for status in statuses
    for hashtag in status['entities']['hashtags']
]

# Compute a collection of all words from all tweets
words = [
    w for t in status_texts
    for w in t.split()
]  # split the string on the empty spaces

# Define a function for computing lexical diversity
def lexical_diversity(tokens):  # This is the way to declare user defined functions
    return 1.0 * len(set(tokens)) / len(tokens)

# Define a function for computing the average number of words per tweet
# Prior to Python 3.0, the division operator (/) applies the floor function and returns an integer value
# (unless one of the operands is a floating-point value).
# Multiply either the numerator or the denominator by 1.0 to avoid truncation errors.
def average_words(statuses):
    total_words = sum([len(s.split()) for s in statuses])
    return 1.0 * total_words / len(statuses)

# Let's use these functions:
print lexical_diversity(words)
print lexical_diversity(screen_names)
print lexical_diversity(hashtags)
print average_words(status_texts)
