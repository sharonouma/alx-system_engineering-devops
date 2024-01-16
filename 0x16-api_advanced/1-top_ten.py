#!/usr/bin/python3
"""
Queries reddit api and returns top ten hot posts
"""

import requests


def top_ten(subreddit):
    headers = {
        "User-Agent": "RedditSubscribers/1.0"
        }
    url = "https://api.reddit.com/r/{}?sort=hot&limit=10".format(subreddit)
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return
        data = response.json()
        for post in data.get("data").get("children"):
            print(post.get("data").get("title"))
    except Exception as e:
        print(None)
        return
