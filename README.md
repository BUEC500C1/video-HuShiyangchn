# video-HuShiyangchn
## This a modified version of video assignment
## The procedure of project 
1. Setting a process list for tweet_user and put the list into a queue then process the user one by one.
2. Get tweets by using tweepy api and store them into json file.

3. Convert the text into image file by using pil library and store them into folder by order. I also set random backround color for different tweets to show the change more easier to notice in the video.

4. Reading the image folder and transfer the images into videos by using ffmpeg.
## The result of processing 
The tweet image looks like this:

![image](https://github.com/BUEC500C1/video-HuShiyangchn/blob/modified/NASA_tweets/NASA16.png)

![image](https://github.com/BUEC500C1/video-HuShiyangchn/blob/modified/realDonaldTrump_tweets/realDonaldTrump10.png)

When every task in queue was completed the program will print out the the current task is finished:

![image](https://github.com/BUEC500C1/video-HuShiyangchn/blob/modified/Image/%E6%88%AA%E5%B1%8F2020-05-09%E4%B8%8B%E5%8D%883.09.14.png)
