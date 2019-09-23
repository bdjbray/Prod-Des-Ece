from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials

class twitterStreamer():  #process the tweets
    def stream_tweets(self,fetched_tweets_filename, hash_tag_list):#choose the place to show our tweets and the keyword used for filter
         #for authtication and connection with twitter stream api
      listener =StdOutListener()  
      auth = OAuthHandler(twitter_credentials.CONSUMER_KEY,twitter_credentials.CONSUMER_SECRET)
      auth.set_access_token(twitter_credentials.ACCESS_TOKEN,twitter_credentials.ACCESS_TOKEN_SECRET)
    
      stream=Stream(auth,listener)
    
      stream.filter(track=hash_tag_list) #use the filter to choose the people I want to listen

class StdOutListener(StreamListener): #inherit streamlistener print tweets to standout
    def init(self,fetched_tweets_filename):
        self.fetched_tweets_filename=fetched_tweets_filename
    def on_data(self,data): #listening from twitts
       try:
           print(data)
           with open(self.fetched_tweets_filename,'a') as tf:
               tf.write(data)
           return True
       except BaseException as e:
           print('Error: %s' % str(e))
       return True
    
    def on_error(self,status):  #what happens when error
        print(status)  #print the error status

if __name__=="__main__":   
    hash_tag_list=["Justin Bieber"]
    fetched_tweets_filename="user1.json"
    
    twitter_streamer=twitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename,hash_tag_list)
    
