'''

Twitter Search API
Tweepy: Twitter Wrapper for Python -- Some uses

Saafi scratch

'''

#import libraries

import tweepy
import pandas as pd


#set up access keys / secrets

creds = pd.read_csv('creds') #store credentials externally in 'creds2'

consumer_key = creds.iloc[0,0] #creds associated with your user access
consumer_secret = creds.iloc[0,1]
access_token = creds.iloc[0,2] #creds associated with your app
access_token_secret = creds.iloc[0,3]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


#test api access
print(api.me().name)


##############################################################
#Examples of streaming use case
##############################################################


from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

# if __name__ == '__main__':
#     l = StdOutListener()
#     auth = OAuthHandler(consumer_key, consumer_secret)
#     auth.set_access_token(access_token, access_token_secret)
#
#     stream = Stream(auth, l)
#     stream.filter(track=['budweiser'])

l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

stream = Stream(auth, l)
stream.filter(track=['Captain Morgan']) #QUESTION: how does one turn this off?


##############################################################
#SEARCH API // TWEEPY: Examples of getting tweets containing terms
##############################################################

import sys
import jsonpickle
import os

searchQuery = 'CaptainMorgan'  # this is what we're searching for
maxTweets = 10000000 # Some arbitrary large number
tweetsPerQry = 100  # this is the max the API permits
fName = 'tweets.txt' # We'll store the tweets in a text file.


# If results from a specific ID onwards are reqd, set since_id to that ID.
# else default to no lower limit, go as far back as API allows
sinceId = None

# If results only below a specific ID are, set max_id to that ID.
# else default to no upper limit, start from the most recent tweet matching the search query.
max_id = -1

tweetCount = 0
print("Downloading max {0} tweets".format(maxTweets))

with open(fName, 'w') as f:
    while tweetCount < maxTweets:
        try:
            if (max_id <= 0):
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry)
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            since_id=sinceId)
            else:
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1))
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1),
                                            since_id=sinceId)
            if not new_tweets:
                print("No more tweets found")
                break
            for tweet in new_tweets:
                f.write(jsonpickle.encode(tweet._json, unpicklable=False) +
                        '\n')
            tweetCount += len(new_tweets)
            print("Downloaded {0} tweets".format(tweetCount))
            max_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            # Just exit if any error
            print("some error : " + str(e))
            break

print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))



tweet._json['text'], tweet._json['created_at']


searchQuery = 'CaptainMorgan'  # this is what we're searching for
maxTweets = 10000000 # Some arbitrary large number
tweetsPerQry = 100  # this is the max the API permits
fName = 'tweets.txt' # We'll store the tweets in a text file.


# If results from a specific ID onwards are reqd, set since_id to that ID.
# else default to no lower limit, go as far back as API allows
sinceId = None

# If results only below a specific ID are, set max_id to that ID.
# else default to no upper limit, start from the most recent tweet matching the search query.
max_id = -1

tweetCount = 0
print("Downloading max {0} tweets".format(maxTweets))

since = '2018-06-06'
until = '2018-06-10'

new_tweets = api.search(q=searchQuery, since=since, until=until)

for tweet in new_tweets:
    print (tweet._json['text'], tweet._json['created_at'])



while tweetCount < maxTweets:
    try:
        if (max_id <= 0):
            if (not sinceId):
                new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                        since=since, until=until)
            else:
                new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                        since=since, until=until)
        else:
            if (not sinceId):
                new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                        max_id=str(max_id - 1),
                                        since=since, until=until)
            else:
                new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                        max_id=str(max_id - 1),
                                        since=since, until=until)
        if not new_tweets:
            print("No more tweets found")
            break
        for tweet in new_tweets:
            print(tweet._json['text'], tweet._json['created_at'])
        tweetCount += len(new_tweets)
        print("Downloaded {0} tweets".format(tweetCount))
        max_id = new_tweets[-1].id
    except tweepy.TweepError as e:
        # Just exit if any error
        print("some error : " + str(e))
        break


#NOTE: ONLY COLLECTS TWEETS FROM LAST 10 DAYS OR SO. TWEEPY DOES NOT APPEAR TO SUPPORT PREMIUM API ACCESS.
#ALTERNATIVE: TRY TWITTERAPI LIBRARY.



'''
TWITTERAPI LIBRARY EXPLORE

https://github.com/geduldig/TwitterAPI

'''

#import TwitterAPI

from TwitterAPI import TwitterAPI
import pandas as pd

#set up access keys / secrets
creds = pd.read_csv('creds') #store credentials externally in 'creds2'

consumer_key = creds.iloc[0,0] #creds associated with your user access
consumer_secret = creds.iloc[0,1]
access_token = creds.iloc[0,2] #creds associated with your app
access_token_secret = creds.iloc[0,3]

api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)


r = api.request('search/tweets', {'q':'pizza'})

for item in r:
        print(item)

since = '2018-06-12'
until = '2018-06-20'

new_tweets = api.search(q=searchQuery, since=since, until=until)


r = api.request('search/tweets', {'q':'pizza', 'since':since, 'until':until})

for tweet in r:
    print (tweet['text'],tweet['created_at'])


from TwitterAPI import TwitterAPI

SEARCH_TERM = 'pizza'
PRODUCT = 'Full-archive'
LABEL = 'your label'


r = api.request('search/tweets', {'query':SEARCH_TERM})

for item in r:
    print(item['text'] if 'text' in item else item)


/search/fullarchive/accounts/:account_name/:label

r = api.request('search/fullarchive/accounts/:Viacom1/:prod.json',
                {'query':SEARCH_TERM})



for item in r:
    print(item['text'] if 'text' in item else item)

########

from TwitterAPI import TwitterAPI

SEARCH_TERM = 'pizza'
PRODUCT = 'fullarchive/accounts/Viacom1'
LABEL = 'prod'


r = api.request('search/fullarchive/accounts/Viacom1/prod', {'query':SEARCH_TERM})

for item in r:
    print(item['text'] if 'text' in item else item)

#################
#Requests
#####################

import requests

import pandas as pd

#set up access keys / secrets
creds = pd.read_csv('creds') #store credentials externally in 'creds2'

#consumer_key = creds.iloc[0,0] #creds associated with your user access
#consumer_secret = creds.iloc[0,1]
#access_token = creds.iloc[0,2] #creds associated with your app
#access_token_secret = creds.iloc[0,3]


user = creds.iloc[0,4]
password = creds.iloc[0,5]

r = requests.get("https://gnip-api.twitter.com/search/fullarchive/accounts/Viacom1/prod.json?query=gnip&maxResults=10",
                 auth=(user, password))

r.status_code
#422

r.raise_for_status()


r.headers['content-type']
#'application/json; charset=utf8'

r.encoding
#'utf-8'

r.text


query_results = r.json()['results']

for item in query_results:
    print(item['created_at'], item['text'])


##################################################
# REQUESTS: GET
##################################################


url_base = 'https://gnip-api.twitter.com/search/fullarchive/accounts/Viacom1/prod.json'
query = '?query=Captain&20Morgan&fromDate=201804300000&toDate=201804300459'
#query = 'query=gnip&maxResults=500&fromDate=<yyyymmddhhmm>&toDate=<yyyymmddhhmm>'

url = url_base+query

r = requests.get(url, auth=(user,password))


r.status_code
#422

r.raise_for_status()


query_results = r.json()['results']

for item in query_results:
    print(item['created_at'], item['user']['screen_name'], item['text'])




##################################################
# REQUESTS: POST
##################################################

url_base = "https://gnip-api.twitter.com/search/fullarchive/accounts/Viacom1/prod.json"
query = '?query=Captain&20Morgan&fromDate=201804300000&toDate=201804300459'

#'{"query":"gnip","maxResults":10}'
r = requests.post(url_base, data = {"query":"gnip","maxResults":10}, auth=(user,password))

r.status_code
#422

r.raise_for_status()




##################################################
##################################################
# GAPI: GNIP API LIBRARY
# Install: pip3 install gapi
# SAAFI NOTE: For Premium Search API, of the options I've evaluated, this seems to be the best library
##################################################
##################################################

from gapi import *
import pandas as pd

#set up access keys / secrets
creds = pd.read_csv('creds') #store credentials externally in 'creds2'

#consumer_key = creds.iloc[0,0] #creds associated with your user access
#consumer_secret = creds.iloc[0,1]
#access_token = creds.iloc[0,2] #creds associated with your app
#access_token_secret = creds.iloc[0,3]

user = creds.iloc[0,4]
password = creds.iloc[0,5]

url_base = 'https://gnip-api.twitter.com/search/fullarchive/accounts/Viacom1/prod.json'

###############
#TWEETS TEXT + METADATA
###############

query_ = gapi.api.Query(user=user,password=password,stream_url=url_base
               , paged = True)

#query_.execute("bieber", 10) #get only 10 tweets

# for x in query_.get_activity_set():
#     print(x)

import datetime

now_date = datetime.datetime.now()
TIME_FORMAT_LONG = "%Y-%m-%dT%H:%M:%S.000Z"
TIME_FORMAT_SHORT = "%Y%m%d%H%M"

query_.execute("budweiser"
               , end='2017-06-23T04:20:02.000Z'
               , start='2017-06-22T19:20:02.000Z'
               , max_results = 999999999999)

for x in query_.get_activity_set():
    print(x)

###############
#COUNTS: daily
###############

query_.execute("budweiser"
               , end='2017-06-15T00:00:00.000Z'
               , start='2017-06-01T00:00:00.000Z'
               , max_results = 999999999999
               , count_bucket = "day")
print(query_)
print(len(query_))

###############
#COUNTS: hourly
###############

query_.execute("budweiser"
               , end='2017-06-23T04:20:02.000Z'
               , start='2017-06-22T19:20:02.000Z'
               , max_results = 999999999999
               , count_bucket = "hour")
print(query_)
print(len(query_))


###############
#COUNTS: by minute
###############

query_.execute("budweiser"
               , end='2017-06-23T04:20:02.000Z'
               , start='2017-06-22T19:20:02.000Z'
               , max_results = 999999999999
               , count_bucket = "minute")
print(query_)
print(len(query_))