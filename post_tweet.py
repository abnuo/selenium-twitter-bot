import os
from twitter_bot_class import TwitterBot

def tweety(text):
    try:
        pj = TwitterBot(os.environ['EMAIL'], os.environ['PASSWORD'])
        pj.login()
        pj.post_tweets(text)
        pj.logout()
    except Exception as e:
        pj.logout()
        print(e)

