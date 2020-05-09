import queue
import time
import multiprocessing
import threading
import subprocess
import tweepy
import wget
import os
import configparser
import datetime
import json
from PIL import Image, ImageDraw, ImageFont

def text2image(twitterText, twitterUsr, twitterNum):
    img = Image.new('RGB', (1920, 1080), color = (0, 0, 0))
    d = ImageDraw.Draw(img)
    d.text((50,20), twitterText, fill=(255, 255, 255))
    fileName = "img/" + twitterUsr + str(twitterNum) + ".png"
    img.save(fileName)


def gettweets(username):
    try:
        f = open('keys')
        # Do something with the file
    except IOError:
        print("No config file")
    finally:
        print('config file exists')
        f.close()
        
    configFilePath = 'keys'
    config = configparser.ConfigParser()
    auth = tweepy.OAuthHandler(config.get('auth', 'consumer_key').strip(),config.get('auth', 'consumer_secret').strip())
    auth.set_access_token(config.get('auth', 'access_token').strip(),config.get('auth', 'access_secret').strip())
    api = tweepy.API(auth)

    tweets = api.user_timeline(username)

    twitterNum = 0
    for tweet in tweets:
        gap = '\n'
        tweet_list = list(tweet.fulltext)
        twitterNum = 0
        for i in range(len(tweet_list)):
            if (i % 50) == 0:
                tweet_list.insert(i,gap)
            # tweet_list.insert(55, gap)
            tweet.text = ''.join(tweet_list)
            print(tweet.text)
            text = tweet.text
        twitterNum += 1
        text2image(text, username, twitterNum)

    # save json file
    tweetcontent= []
    for status in tweepy.Cursor(api.user_timeline,id=username,count = 20,tweet_mode='extended').items(20):
        tweetcontent.append(status.full_text)

    file = open('jsonFolder/' + username+'.json', 'w')
    json.dump(tweetcontent,file,indent = 4)
    file.close()


def loaclconvert(username):
    # read Json file one by one
    with open('jsonFolder/' + username +'.json') as json_data:
        data_dict = json.load(json_data)
        num = 0
        for line in data_dict:
            text2image(line, username, num)
            num += 1


def img2Video(twitterUsr):
  fileName = "img/" + twitterUsr + "%01d" + ".png"
  normalVideo = "output/" + twitterUsr + "normal.avi"
  betterVideo = "output/" + twitterUsr + "better.mp4"

  subprocess.call(['ffmpeg', '-framerate', '0.3', '-i', 
    fileName, 
    normalVideo])

  subprocess.call(['ffmpeg', '-i', normalVideo, '-c:a', 'copy', 
    '-c:v', 'copy', '-r', '30', '-s', 'hd720', '-b:v', '2M', 
    betterVideo])

q = queue.Queue()
num_threads = 4
threads = []
usernames = ['BU_Tweets', 'realDonalTrump', 'Google','amazon','BU_ece']


def workline():
    while True:
        counter = 0
        item=q.get()
        if item is None:
            print ('No current item exist')
            counter = 0
        # break
        counter= counter + 1
        print("The process" +str(counter) +"is processing")
        gettweets(item)
        img2Video(item)
        print("The item is finished")
        q.task_done()

for item in usernames:
    q.put(item)

for i in range (num_threads):
    t = threading.Thread(target= workline)
    t.daemon = True
    t.start()
    threads.append(t)
q.join()

for j in range(num_threads):
    q.put(None)
for k in threads:
    t.join()
