# video-HuShiyangchn
## This a modified version of video assignment
## The procedure of project 
1. Setting a process list for tweet_user and put the list into a queue then process the user one by one.
2. Get tweets by using tweepy api and store them into json file. If internet connection is not avavilable it will read local json file isntead.

3. Convert the text into image file by using pil library and store them into folder by order. I also set random backround color for different user.

4. Reading the image folder and transfer the images into videos by using ffmpeg.
## The authentication data
The key for twitter api should be store in key file the program will automatically parse the file and read the key.</br>
[auth]    
consumer_key = </br>
consumer_secret = </br>
access_token = </br>
access_token_secret= </br>
The key after equal sign should not have quotation marks otherwise it will cause mistake to parse the key. Just like this:</br>
consumer_key = asdfsdafsadfasdf</br>
not:</br>
consumer_key = 'asdfsdafsadfasdf'</br> or 
consumer_key = "asdfsdafsadfasdf"
Plus if the key is empty the program will try to load local json file the get tweets.
## The result of processing 
The tweet image looks like this:

![image](https://github.com/BUEC500C1/video-HuShiyangchn/blob/modified/NASA_tweets/NASA16.png)

![image](https://github.com/BUEC500C1/video-HuShiyangchn/blob/modified/realDonaldTrump_tweets/realDonaldTrump10.png)

When every task in queue was completed the program will print out the the current task is finished:

![image](https://github.com/BUEC500C1/video-HuShiyangchn/blob/modified/Image/%E6%88%AA%E5%B1%8F2020-05-09%E4%B8%8B%E5%8D%883.09.14.png)

## Other attention
Not working on windows for glob.h file lost of win ffmpeg. So on windows it is hard to go through the image folder by order and generate the video file.