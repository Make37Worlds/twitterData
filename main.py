import tweepy
from kafka import KafkaProducer
import json

# Twitter API credentials
consumer_key = 'busrmTCDSoeO1R8VqthJu12zG'
consumer_secret = '6Mf8Ib1ssBTSJS1DR9xgJfwLrHQFGbreuT80x7bHFDDNS91Ekb'
access_token = '1720280708693008385-YEca7b4P4gs4IdINxApoaYeEeaZZn4'
access_token_secret = 'ly40OogmrlT0TzkWjqxi0zZSnCvWtkO1SD1qgIziQlP8k'

# Kafka configuration
kafka_topic = 'twitter_topic'
kafka_broker = 'localhost:9092'  # Change this to your Kafka broker

# Tweepy setup
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Kafka producer
producer = KafkaProducer(bootstrap_servers=kafka_broker,
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

class TwitterStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        tweet = status._json
        producer.send(kafka_topic, tweet)
        print(f"Tweet sent to kafka topic '{kafka_topic}'")

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False

# Initialize stream listener
listener = TwitterStreamListener()
stream = tweepy.Stream(auth=api.auth, listener=listener)

# Start streaming tweets
stream.filter(track=['#exampleHashtag'], languages=['en'])  # Customize this filter