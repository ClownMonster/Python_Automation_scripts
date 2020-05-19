'''
This scripts gets the followers of the required twitter account

'''

import tweepy


auth  = tweepy.OAuthHandler(consumer_key = "REMOVED", consumer_secret = "REMOVED")
auth.set_access_token(key = "REMOVED", secret = "REMOVED") 

api = tweepy.API(auth)
user  = tweepy.api.get_user()
print(user.screen_name)

