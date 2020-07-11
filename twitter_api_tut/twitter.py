import tweepy
import time

auth  = tweepy.OAuthHandler('ECDpZsao2nvABSH9EZqkO0srV', 'T7rw50SdltpcTe4Gw7jaJbQaxgQlYE3wWmMUAlGF2foMZLc977')
auth.set_access_token('1280167743149551621-Vw4ASQHL6uCc6qUPw6u66UVSLCtS2G', 'S46REsXSNyiLn0S2dQWFuIO1RG5BRBABls0AuRNDZQyeJ')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'Python'
nrTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

#for follower in tweepy.Cursor(api.followers).items():
#   print(follower.name)