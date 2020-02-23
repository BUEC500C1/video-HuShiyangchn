import tweepy
import wget
import os
import datetime
#import urllib2

tweetsnum = 10
consumer_key = "5BPSMCofACuMtRLPEWM5RGQoO"
consumer_secret = "oKr8gArD2uwgOz4cnFzw7JqmmMyX51o3oMOkl5fhWSR591Gs1F"
access_token ="1227718321874669568-tjbyvDD73So1buu8Wx8kPKSJBj8GJb"
access_token_secret="TceCoqwG0MtaaXDxjSSxPyCtGURSs4aMc4b5rMw2zTZJZ"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
tweets = api.user_timeline('nytimes',count=tweetsnum, tweet_mode='extended')

media_files = set()

for status in tweets:
    media = status.entities.get('media', [])
    if(len(media) > 0):
        media_files.add(media[0]['media_url'])

for media_file in media_files:
    wget.download(media_file)

direct = os.getcwd()
tweetdir = os.path.join(direct,'tweets')

contentlist = []
#print(tweets)
for tweet in tweets:
    if (tweet.created_at.date() == datetime.date.today()):
        contentlist.append(tweet.full_text)
        #fileobject.write('\n')
for items in contentlist:
    print(items, end=' ')

for i in range(len(contentlist)):
    filename = 'tweet%s.txt' %(i)
    filepath = os.path.join(tweetdir,filename)
    with open(filepath,'w') as fileobject:
        fileobject.write(contentlist[i])
        #for tweet in tweets: