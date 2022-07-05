import tweepy
from datetime import datetime

class TwitterClient:
    def __init__(self):
        twitter_auth_keys = {
            "consumer_key"        : "gdyrRvbHejSwozbsqp3MQdEGA",
            "consumer_secret"     : "MVdGaXmvkeM6WpU4CSmR79Pcq3JIxdQYxISNNvQyO9ptN3hC7S",
            "access_token"        : "1536717264346660865-6vT9SSckSyoeP4at9fIvvmFckbgw2j",
            "access_token_secret" : "LRPQRtpkzyo6e4hLyIkHIPoQjItuAIImyVb45T8k6NkDf"
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
