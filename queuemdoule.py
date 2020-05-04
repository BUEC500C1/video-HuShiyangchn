import queue
import time
import multiprocessing
import threading
import subprocess
import tweepy
import wget
import os
import datetime
def loaclconvert(username):
  # read Json file one by one
  with open('jsonFolder/' + twitterUsr +'.json') as json_data:
    # save json data in a dictionary
    data_dict = json.load(json_data)
    highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    num = 0
    for line in data_dict:
      textToImg(line, twitterUsr, num)
      num += 1

def gettweets(username):
    try:
        f = open('keys')
        # Do something with the file
    except IOError:
        print("File not accessible")
    finally:
        print('keys file exists')
        f.close()
    #read key from config file
    config = configparser.ConfigParser()
    auth = tweepy.OAuthHandler(config.get('auth', 'consumer_key').strip(),config.get('auth', 'consumer_secret').strip())
    auth.set_access_token(config.get('auth', 'access_token').strip(),config.get('auth', 'access_secret').strip())
    api = tweepy.API(auth)

    tweets = api.user_timeline(username)

    twitterNum = 0
    highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    for tweet in tweets:
        gap = '\n'
        tweet_list = list(tweet.fulltext)

        list_num = 0
        for i in range(len(tweet_list)):
            if (i % 50) == 0:
                tweet_list.insert(i,gap)
            # tweet_list.insert(55, gap)
            tweet.text = ''.join(tweet_list)
            print(tweet.text)

        # convert format of text
        text_noem = highpoints.sub('--emoji--', tweet.text)
        text_noem = text_noem.encode('utf8')

        # add 1 for number of images
        twitterNum += 1

        textToImg(text_noem, username, twitterNum)

    # save json file
    tweetcontent= []
    for status in tweepy.Cursor(api.user_timeline,id=username,count = 20,tweet_mode='extended').items(20):
        tweetcontent.append(status.full_text)

    #write tweet objects to JSON
    file = open('jsonFolder/' + username+'.json', 'w')
    print ("Writing tweet objects to JSON file, please wait...")
    json.dump(tweetcontent,file,indent = 4)
    print ("Done")
    file.close()

def textToImg(twitterText, twitterUsr, twitterNum):
  # convert / write text on image
  img = Image.new('RGB', (400, 150), color = (0, 0, 0))
  d = ImageDraw.Draw(img)
  d.text((50,20), twitterText, fill=(255, 255, 255))
  fileName = "img/" + twitterUsr + str(twitterNum) + ".png"
  img.save(fileName)


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
        apimodule(item)
        text2image(item)
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

'''
def main():
    q = queue.Queue()
    num_threads = 4
    threads = []
    usernames = ['BU_Tweets', 'realDonalTrump', 'Google','amazon','BU_ece']
    multithreading()

if __name__ == "__main__":
    main()

'''

'''
def worker():
  while True:
    item = q.get()

    numb = 0
    qSize = q.qsize()
    if item is None:
      print("No item now, please put in some stuff!")
      numb = 0
      break

    numb += 1
    print("Currently process on " + str(numb) + " from current " + str(qSize) + " items")
    #do_work(item)
    # after get all images, then get videos
    tweepy_info(item) 
    imgToVideo(item)

    print("Current worker is finished.")
    
    q.task_done()
'''