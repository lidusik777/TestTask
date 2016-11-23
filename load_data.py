#!/usr/bin/env python
import tweepy, webbrowser
import twitter

# Consumer keys and access tokens, used for OAuth
CONSUMER_KEY = 'pJFCiWi9ktQuqJytLltumxiYQ'
CONSUMER_SECRET = 'nAP5OCcQMla0LjPpLyB1c4vIU6y76qSPVHilYRfYnZw7PoctAU'
ACCESS_KEY = '202322731-itJ81UdohlJYFnTc64GSxo9ZEAPPHumNuU9QkQHD'
ACCESS_SECRET = 'khq9s8J0rMmoN9Zj59EJXPSYLiPguJeh7j5dxIyynK7xP'



class StdOutListener():
    ''' Handles data received from the stream. '''

    def on_status(self, status):
        # Prints the text of the tweet
        print('Tweet text: ' + status.text)

        # There are many options in the status object,
        # hashtags can be very easily accessed.
        for hashtag in status.entries['hashtags']:
            print(hashtag['text'])

        return true

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True  # To continue listening

    def on_timeout(self):
        print('Timeout...')
        return True  # To continue listening

if __name__ == '__main__':
    listener = StdOutListener()
    # OAuth process, using the keys and tokens
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    # Creation of the actual interface, using authentication
    api = tweepy.API(auth)
    api.update_status('Hello Python Central!')
    user = api.me()

    print('Name: ' + user.name)
    print('Location: ' + user.location)
    print('Friends: ' + str(user.friends_count))
    stream = tweepy.Stream(auth, listener)
    stream.filter(follow=[38744894], track=['#pythoncentral'])
# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# auth_url = auth.get_authorization_url()
# webbrowser.open(auth_url)
# verifier = raw_input('PIN: ').strip()
# auth.get_access_token(verifier)
# print "ACCESS_KEY = '%s'" % auth.access_token.key
# print "ACCESS_SECRET = '%s'" % auth.access_token.secret
# import twitter
# from twitter import Twitter
# print(twitter.__file__)
#
# exit()



# Setting up Twitter API
# twitter2 = Twitter(
#       auth=OAuth(token, token_key, con_secret, con_secret_key))

# Get the public timeline
# twitter.statuses.public_timeline()

# api = twitter.Api(
#     consumer_key='pJFCiWi9ktQuqJytLltumxiYQ',
#     consumer_secret='nAP5OCcQMla0LjPpLyB1c4vIU6y76qSPVHilYRfYnZw7PoctAU',
#     access_token_key='	202322731-itJ81UdohlJYFnTc64GSxo9ZEAPPHumNuU9QkQHD',
#     access_token_secret='khq9s8J0rMmoN9Zj59EJXPSYLiPguJeh7j5dxIyynK7xP'
# )
# search = api.GetSearch(term='CELYAD SA', lang='en', result_type='recent', count=100, max_id='')
# for t in search:
#     print t.user.screen_name + ' (' + t.created_at + ')'
#     # Add the .encode to force encoding
#     print t.text.encode('utf-8')
#     print ''
# client = twitter.Api()
