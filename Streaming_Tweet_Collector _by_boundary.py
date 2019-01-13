from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time


#consumer key, consumer secret, access token, access secret.
#Irfan's key 
ckey=''
csecret=''
atoken=''
asecret=''


class listener(StreamListener):

    def on_data(self, data):
        try:
            print('Running----------------------------by location----')
            saveFile= open('AI_StormHarvey_Boundary.json', 'a')
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
twitterStream.filter(locations=[-108.00,24.00,-92.00,40])
