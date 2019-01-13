from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

#consumer key, consumer secret, access token, access secret.

twitter_app_auth = {
    'consumer_key': '',
    'consumer_secret': '',
    'access_token': '',
    'access_token_secret': '',
}
ckey=twitter_app_auth['consumer_key']
csecret=twitter_app_auth['consumer_secret']
atoken=twitter_app_auth['access_token']
asecret=twitter_app_auth['access_token_secret']



class listener(StreamListener):
    

    def on_data(self, data):
        
        try:

            all_data = json.loads(data)
            tweet = all_data["text"]
            sentiment_value, confidence = s.sentiment(tweet)
            print(sentiment_value, confidence)
    
            if confidence*100 >= 80:
                    output = open("twitter-out.txt","a")
                    output.write(sentiment_value)
                    output.write('\n')
                    output.close()
                    return True
        
        except :
            print('failed on data')
            time.sleep(3)

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["USA"])
