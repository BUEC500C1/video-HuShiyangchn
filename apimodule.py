import tweepy
import wget

filename="output.txt"


consumer_key = "5BPSMCofACuMtRLPEWM5RGQoO"
consumer_secret = "oKr8gArD2uwgOz4cnFzw7JqmmMyX51o3oMOkl5fhWSR591Gs1F"
access_token ="1227718321874669568-tjbyvDD73So1buu8Wx8kPKSJBj8GJb"
access_token_secret="TceCoqwG0MtaaXDxjSSxPyCtGURSs4aMc4b5rMw2zTZJZ"

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
