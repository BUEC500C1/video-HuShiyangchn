import tweepy
import wget

filename="output.txt"


consumer_key = ""
consumer_secret = ""
access_token =""
access_token_secret=""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = api.user_timeline('LeoDiCaprio')

media_files = set()
for status in tweets:
    media = status.entities.get('media', [])
    if(len(media) > 0):
        media_files.add(media[0]['media_url'])

for media_file in media_files:
    wget.download(media_file)
with open(filename,'w') as fileobject:
    for tweet in tweets:
        fileobject.write(tweet.text)
        fileobject.write('\n')
