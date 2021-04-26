from textblob import TextBlob
import sys
import tweepy
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('PUBLIC_API')
api_key_secret = os.getenv('PRIVATE_API')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

auth_handler = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
auth_handler.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth_handler=auth_handler)

search_term = 'stocks'
tweet_amount = 200

tweets = tweepy.Cursor(api.search, q=search_term, lang='en').items(tweet_amount)

polarity = 0
positive = 0
neutral = 0
negative = 0

for tweet in tweets:
    # preprocessing
    final_text = tweet.text.replace('RT', '')
    if final_text.startswith(' @'):
        position = final_text.index(':')
        final_text = final_text[position+2:]
    if final_text.startswith(' @'):
        position = final_text.index(' ')
        final_text = final_text[position+2:]
    # print(final_text)

    # analysis
    analysis = TextBlob(final_text) 
    tweet_polarity = analysis.polarity
    if tweet_polarity > 0.00 :
        positive += 1
    elif tweet_polarity < 0.00 :
        negative += 1
    elif tweet_polarity == 0.00:
        neutral += 1
    polarity += analysis.polarity


print(polarity)
print(f'Amount of positive tweets : {positive}')
print(f'Amount of negative tweets : {negative}')
print(f'Amount of neutral tweets : {neutral}')