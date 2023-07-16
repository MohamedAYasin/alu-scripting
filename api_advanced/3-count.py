#!/usr/bin/python3
"""
word count function
"""
import json
import requests


def count_words(subreddit, word_list, after="", count=None):
    """ returns a sorted count of given keywords """
    
    if count is None:
        count = {word.lower(): 0 for word in word_list}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    request = requests.get(url,
                           params={'after': after},
                           allow_redirects=False,
                           headers={'User-Agent': 'Mozilla/5.0'})

    if request.status_code == 200:
        data = request.json()

        for topic in data['data']['children']:
            for word in topic['data']['title'].split():
                word = word.lower()
                if word in count:
                    count[word] += 1

        after = data['data']['after']
        if not after:
            sorted_counts = sorted(count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                if count > 0:
                    print("{}: {}".format(word, count))
        else:
            count_words(subreddit, word_list, after, count)

# Example usage:
if __name__ == "__main__":
    subreddit = "unpopular"
    word_list = ['you', 'unpopular', 'vote', 'down', 'downvote', 'her', 'politics']
    count_words(subreddit, word_list)
