#!/usr/bin/python3
"""
Queries reddit api and returns number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    headers = {
        "User-Agent": "RedditSubscribers/1.0"
        }
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0
        data = response.json()
        subscribers = data.get("data").get("subscribers")
        return subscribers
    except Exception as e:
        return 0
