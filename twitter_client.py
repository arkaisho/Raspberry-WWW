import tweepy
from datetime import datetime

class TwitterClient:
    def __init__(self):
        twitter_auth_keys = {
            "consumer_key"        : "",
            "consumer_secret"     : "",
            "access_token"        : "",
            "access_token_secret" : ""
        }
    
        auth = tweepy.OAuthHandler(
                twitter_auth_keys['consumer_key'],
                twitter_auth_keys['consumer_secret']
                )
        auth.set_access_token(
                twitter_auth_keys['access_token'],
                twitter_auth_keys['access_token_secret']
                )
        self.api = tweepy.API(auth)

 
    def post(self,text):
        try:
            status = self.api.update_status(status=text+" ("+self.getFormattedDateTime()+")")
        except:
            print("twitter duplicated")
    
    def getFormattedDateTime(self):
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
