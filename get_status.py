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
  
id = 1539031248638812160
  
status = api.get_status(id, tweet_mode = "extended")
  
full_text = status.full_text 
  
print("The text of the status is : \n\n" + full_text)
file = open("tweet.txt","w")
file.write(full_text)
file.close()

  
