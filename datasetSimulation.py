from kafka import KafkaProducer
import pandas as pd
import json
import random
import time

kafka_broker = 'localhost:9092'

# Initialize the Kafka producer
producer = KafkaProducer(bootstrap_servers=kafka_broker,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Load the dataset of tweets
tweets_df = pd.read_csv('datasets/trumptweets1205-127.csv')


# Function to simulate sending tweets to Kafka as if in real-time
def simulate_tweets_stream(producer, topic, tweets):
    for index, row in tweets.iterrows():
        # Generate a random view count for each tweet
        views = random.randint(1000, 1000000)

        # Construct the message as a dictionary
        message = {
            'Tweetid': row['Tweetid'],
            'Date': row['Date'],
            'Tweet': row['Tweet'],
            'Views': views
        }

        producer.send(topic, value=message)
        producer.flush()
        print(f"Tweet with ID: {row['Tweetid']} and {views} views sent to Kafka topic: {topic}")

        # Sleep to simulate real-time streaming; you can adjust this as needed
        time.sleep(1)


simulate_tweets_stream(producer, 'test', tweets_df)