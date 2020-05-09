import tweepy
import queue
import multiprocessing
import threading
import configparser
import ffmpeg
from PIL import Image,ImageDraw
import os
import glob
import json
import random

class final:

  def __init__(self,path, process_list):
    self.process_list = process_list
    self.api = self.authentication(path)
    self.que = queue.Queue()
    self.threads = []
    self.thread_amount = 4
    self.threadProcess(process_list)

  def threadProcess(self, process_list):
    for each in process_list:
      self.que.put(each)
    for i in range(self.thread_amount):
      t = threading.Thread(target = self.processor())
      t.daemon = True
      t.start()
    print('The queue is clean')
    self.que.join()
    for i in range(self.thread_amount):
        self.que.put(None)
    for t in self.threads:
        t.join()

  def processor(self):
    while True:
      element = self.que.get()
      if element is None:
        print('Queue is Empty!!!')
        break
      self.getTweets(element)
      self.que.task_done()
      print('Processing the No. ' + str(self.process_list.index(element) + 1) + ' task of ' + str(len(self.process_list)) + ' tasks')

  def authentication(self,path):
    if not os.path.exists(path):
      return None
    else:   
      config = configparser.ConfigParser()
      config.read(path)
      auth = tweepy.OAuthHandler(config.get('auth', 'consumer_key'),
                                 config.get('auth', 'consumer_secret'))
      print()
      auth.set_access_token(config.get('auth', 'access_token'),
                            config.get('auth', 'access_token_secret'))
      api = tweepy.API(auth)
    return api

  def getTweets(self,user_name):
    temp = {}
    counter = 0
    tweet_list = []
    if self.api == None:
      with open(user_name) as json_file:
        data = json.load(json_file)
        return data[user_name]
    tweets = self.api.user_timeline(id = user_name, count = 30)
    for tweet in reversed(tweets):
      for character in tweet.text:
        if ord(character) > 256:
          tweet.text = tweet.text.replace(character, " ")
      tweet = tweet.text 
      if user_name in temp:
        temp[user_name] += [tweet]
      else:
        temp[user_name] = []
      tweet_list.append(tweet)
    with open(user_name, 'w+') as outfile:
      json.dump(temp, outfile)
    return self.text2Image(tweet_list,counter,user_name)
    
  def getRandomColor(self):
    c1 = random.randint(0,255)
    c2 = random.randint(0,255)
    c3 = random.randint(0,255)
    return (c1,c2,c3)

  def text2Image(self,tweet_list,counter,user_name):
    if not os.path.isdir(user_name + '_tweets'):
      os.mkdir(user_name + '_tweets')
    while counter < len(tweet_list):
      pre_image = Image.new(mode = 'RGB', size = (1024,720), color = self.getRandomColor())
      image = ImageDraw.Draw(pre_image)
      image.text((50,200), tweet_list[counter], fill = (255,255,255))
      fileName = user_name + '_tweets/'+ user_name + str(counter) + '.png'
      pre_image.save(fileName)
      counter += 1
    return self.image2Video(user_name)

  def image2Video(self,user_name):
    if not os.path.isdir('daily_videos'):
      os.mkdir('daily_videos')
    fileName = os.getcwd() + '/' + user_name + '_tweets/' + '*.png'
    videoName = 'daily_videos/' + user_name + '_daliy.mp4'
    ffmpeg.input(fileName, pattern_type = 'glob', framerate = 0.3).output(videoName).run()

def main():
  final('keys',['BU_tweets','NASA','Google','realDonaldTrump'])

if __name__ == '__main__':
    main()