import tweepy
import os
import time

# https://dev.to/biplov/handling-passwords-and-secret-keys-using-environment-variables-2ei0

from dotenv import load_dotenv
load_dotenv()

# api keys
consumer_key = os.environ.get('consumer_key')
consumer_secret = os.environ.get('consumer_secret')
access_token = os.environ.get('access_token')
access_token_secret = os.environ.get('access_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

# for tweet in public_tweets:
#     print(tweet.text)

user = api.me()
# print(user.screen_name)


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(3)

search_string = 'python'
numbersOfTweets = 2
for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


# Follow Bot
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     if follower.name == '국카스텐(Guckkasten)':
#         follower.follow()
    # print(follower.name)

