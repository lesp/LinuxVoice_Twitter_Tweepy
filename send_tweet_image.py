import tweepy
from time import sleep
import sys
import easygui as eg

consumer_key = "YOUR API KEY"
consumer_secret = "YOUR API SECRET"
access_token = "YOUR TOKEN"
access_token_secret = "YOUR TOKEN SECRET"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
image = eg.fileopenbox(title="Pick an image to attach to your tweet")
message = eg.enterbox(title="Send a tweet", msg="What message would you like to send?")
try:
	length = len(message)
	if length < 140:
		api.update_with_media(image, status=message)
		#api.update_status(message)
	else:
		eg.msgbox(msg="Your tweet is too long. It is "+str(length)+" characters long")
except:
	sys.exit()