#Import the libraries that we need.
import tweepy
from time import sleep
import sys
import easygui as eg

#Replace the placeholder text with your unique keys and tokens
consumer_key = "YOUR API KEY"
consumer_secret = "YOUR API SECRET"
access_token = "YOUR TOKEN"
access_token_secret = "YOUR TOKEN SECRET"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def timeline():
        public_tweets = api.home_timeline()
        for tweet in public_tweets:
                try:
                        tweets = eg.buttonbox(title="Your timeline", msg=tweet.text, choices=("More","Exit"))
                        if tweets != "More":
                                break
                except:
                        print("Exiting")
                        sys.exit()

def send_tweet():
        message = eg.enterbox(title="Send a tweet", msg="What message would you like to send?")
        try:
                length = len(message)
                if length < 140:
                        api.update_status(message)
                else:
                        eg.msgbox(msg="Your tweet is too long. It is "+str(length)+" characters long")
        except:
                sys.exit()

def send_image():
        image = eg.fileopenbox(title="Pick an image to attach to your tweet")
        message = eg.enterbox(title="Send a tweet", msg="What message would you like to send?")
        try:
                length = len(message)
                if length < 140:
                        api.update_with_media(image, status=message)
                else:
                        eg.msgbox(msg="Your tweet is too long. It is "+str(length)+" characters long")
        except:
                sys.exit()


#Main Menu
while True:
        choice = eg.choicebox(title="Linux Voice Twitter App", choices=("Read my timeline","Send tweet", "Tweet with image", "Exit"))
        if choice == "Read my timeline":
                timeline()
        elif choice == "Send tweet":
                send_tweet()
        elif choice == "Tweet with image":
                send_image()
        else:
                sys.exit()
else:
        sys.exit()
