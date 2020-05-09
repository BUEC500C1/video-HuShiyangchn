# video-HuShiyangchn
## This a modified version of video assignment
## The procedure of project 
1. Setting a process list for tweet_user and put the list into a queue then process the user one by one.
2. Get tweets by using tweepy api and store them into json file.

3. Convert the text into image file by using pil library and store them into folder by order. I also set random backround color for different user.

4. Reading the image folder and transfer the images into videos by using ffmpeg.
## The result of processing 
When every task in queue was completed the program will print out the the current task is finished:

![imgae]()