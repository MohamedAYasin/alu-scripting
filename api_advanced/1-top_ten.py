#!/usr/bin/python3
"""
1-top_ten.py: Top Ten

This module contains a function that queries the Reddit API and prints the
titles of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Prints the top ten hot posts for a given subreddit"""

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get("data")
    if data is None or len(data.get("children")) == 0:
        print(None)
        return

    for child in data.get("children"):
        print(child.get("data").get("title"))
