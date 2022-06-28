
import tweepy

class TwitterClient:
    def __init__(self):
        pass

 
    def post(self):
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
        api = tweepy.API(auth)
    
        tweet = "Testing post for IoT project"
        status = api.update_status(status=tweet)
    


twitterCLient = TwitterClient()

twitterCLient.post()