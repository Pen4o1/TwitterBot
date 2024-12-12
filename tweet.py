import tweepy
import os

from dotenv import load_dotenv, dotenv_values
load_dotenv()
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
   
api = tweepy.API(auth)
tweet ="Text part of the tweet" 
image_path ="path of the image"
  
status = api.update_with_media(image_path, tweet) 
api.update_status(status = tweet)