import tweepy

# Twitter API credentials
consumer_key = 'busrmTCDSoeO1R8VqthJu12zG'
consumer_secret = '6Mf8Ib1ssBTSJS1DR9xgJfwLrHQFGbreuT80x7bHFDDNS91Ekb'
access_token = '1720280708693008385-YEca7b4P4gs4IdINxApoaYeEeaZZn4'
access_token_secret = 'ly40OogmrlT0TzkWjqxi0zZSnCvWtkO1SD1qgIziQlP8k'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAABzWtQEAAAAA8Bxcyo8gyNBvBjozv8aaBUJnu%2Bk%3D7QSRvOy2Y74kcxaXZGJ2rgzXJqUIjD8epUaOrMXuw51WnreVW0'

class PrintListener(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        # Handle the tweet here
        print(tweet.text)

# Initialize the listener with your Bearer Token
listener = PrintListener(bearer_token)

# Define the rules for the stream - adjust as needed
# For example, to follow tweets from a specific account (TwitterDev) or containing a hashtag (#examplehashtag)
rules = [
    tweepy.StreamRule("from:TwitterDev"),
    tweepy.StreamRule("#examplehashtag")
]

# Adding rules to the stream - This replaces all existing rules
current_rules = listener.get_rules()
if current_rules.data:
    listener.delete_rules([rule.id for rule in current_rules.data])

listener.add_rules(rules)

# Use the filter method with no parameters to receive all matching tweets per the rules
listener.filter()