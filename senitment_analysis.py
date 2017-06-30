import os
import json
from pattern.en import positive, sentiment

file_name = 'final_data/washington.txt'
positive_file = 'positive/washington.txt'
negative_file = 'negative/washington.txt'
positive_tweets = []
negative_tweets = []
with open(file_name) as in_file:
    for line in in_file:
        tweet = line

        if positive(tweet):
            positive_tweets.append(tweet)
        else:
            negative_tweets.append(tweet)

with open(positive_file, 'w') as out_file:
    for tweet in positive_tweets:
        out_file.write(tweet)
        out_file.write("\n")

with open(negative_file, 'w') as out_file:
    for tweet in negative_tweets:
        out_file.write(tweet)
        out_file.write("\n")