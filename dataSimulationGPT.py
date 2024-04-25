import openai
import os
import json
from datetime import datetime
import random

from openai import OpenAI

# Step 1: Define your API key (normally you would get this from a secure environment variable)
client = OpenAI(
    # This is the default and can be omitted
    api_key="sk-proj-WwHEZylU5SVb6DcLvaNmT3BlbkFJKwOc27746FCyez45RTRV",
)


# Step 2: Define the fixed format for your Twitter data
def create_tweet_structure(username, content, retweets, likes, timestamp):
    return {
        "user": username,
        "text": content,
        "retweets": retweets,
        "likes": likes,
        "timestamp": timestamp
    }


# Step 3: Generate tweet content using OpenAI's API
def generate_tweet_content(topic):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Write a creative tweet about {topic}."}
        ]
    )
    tweet_text = response['choices'][0]['message']['content']
    return tweet_text.strip()


# Step 4: Simulate a series of tweets on a hot topic
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


# Step 5: Main function to run the simulation
def main():
    topic = "self-driving cars"
    num_tweets = 10  # The number of tweets to simulate
    simulated_tweets = simulate_hot_topic(topic, num_tweets)

    # Output the simulated tweets in the fixed format
    for tweet in simulated_tweets:
        print(json.dumps(tweet, indent=2))


if __name__ == "__main__":
    main()