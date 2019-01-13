from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time


#consumer key, consumer secret, access token, access secret.
ckey=''
csecret=''
atoken=''
asecret=''


class listener(StreamListener):

    def on_data(self, data):
        try:
            print('Running--------------------------------')
            saveFile = open("twitter-out.txt","a")
            #saveFile= open('Maria.json', 'a')
            saveFile.write(data)
            #saveFile.write('\n')
            saveFile.close()
            return(True)
        except BaseException:
            print ('failed on data')
            time.sleep(5)
        

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["bangladesh"])
