import random
from datetime import datetime
from transformers import pipeline
import torch

# Step 1: Define the tweet structure
def create_tweet_structure(username, content, retweets, likes, timestamp):
    return {
        "user": username,
        "text": content,
        "retweets": retweets,
        "likes": likes,
        "timestamp": timestamp
    }

# Step 2: Generate tweet content using a pre-trained generative model
# Replace "model_name" with "gpt2" or another pre-trained model of your choice.
generator = pipeline("text-generation", model="gpt2")

def generate_tweet_content(topic):
    prompt = f"Write a creative tweet about {topic}."
    response = generator(prompt, max_length=280, num_return_sequences=1)  # Limit the tweet length to 280 characters
    tweet_text = response[0]['generated_text'].strip()
    return tweet_text

# Step 3: Simulate tweets
def simulate_hot_topic(topic, num_tweets):
    tweets = []
    for _ in range(num_tweets):
        username = f"user{random.randint(1, 10000)}"
        tweet_content = generate_tweet_content(topic)
        retweets = random.randint(0, 1000)
        likes = random.randint(0, 5000)
        timestamp = datetime.now().isoformat()
        tweet = create_tweet_structure(username, tweet_content, retweets, likes, timestamp)
        tweets.append(tweet)
    return tweets

# Step 4: Main function
def main():
    topic = "self-driving cars"
    num_tweets = 10  # The number of tweets to simulate
    simulated_tweets = simulate_hot_topic(topic, num_tweets)

    # Output tweets with text and retweets only
    for tweet in simulated_tweets:
        print(f"Text: {tweet['text']}\nRetweets: {tweet['retweets']}\n")

if __name__ == "__main__":
    main()