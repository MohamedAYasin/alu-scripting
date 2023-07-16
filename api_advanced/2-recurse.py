#!/usr/bin/python3
"""
2. Recurse it!
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ function that queries the Reddit API and returns a list containing
        the titles of all hot articles for a given subreddit. If no results
        are found for the given subreddit, the function should return None.
    """
    headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0)\
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100\
                Safari/537.36'}
    params = {'limit': 100, 'after': after}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    res = requests.get(url, headers=headers, params=params)
    if res.status_code == 404:
        return None
    children = res.json().get('data').get('children')
    for child in children:
        hot_list.append(child.get('data').get('title'))
    after = res.json().get('data').get('after')
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
