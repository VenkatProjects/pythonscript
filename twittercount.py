#!/bin/python

import tweepy

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler("consumer_key", "consumer_secret")
auth.set_access_token("access_token", "access_token_secret")

# Create a Twitter API client
api = tweepy.API(auth)

# Get the user's Twitter handle
handle = input("Enter the Twitter handle: ")

# Get the user's Twitter profile information
user = api.get_user(handle)

# Get the user's follower count
follower_count = user.followers_count

# Print the follower count
print("The number of followers for", handle, "is", follower_count)


