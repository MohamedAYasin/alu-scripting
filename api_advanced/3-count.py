#!/usr/bin/python3
import json
import requests

def count_words(subreddit, word_list, after=None, counts=None):
    """ Recursive function to query the Reddit API and count given keywords """

    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100}
    if after:
        params['after'] = after

    request = requests.get(url, params=params, allow_redirects=False, headers={'User-Agent': 'Mozilla/5.0'})

    if request.status_code == 200:
        data = request.json()

        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                title = post['data']['title'].lower()

                for word in word_list:
                    if f' {word.lower()} ' in f' {title} ':
                        counts[word.lower()] = counts.get(word.lower(), 0) + title.count(f' {word.lower()} ')

            after = data['data']['after']
            if after:
                return count_words(subreddit, word_list, after, counts)
            else:
                sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_counts:
                    if count > 0:
                        print(f"{word}: {count}")
        else:
            print("No data found for the given subreddit.")
    else:
        print(f"Error fetching data for the subreddit: {subreddit}")

# Example usage:
if __name__ == "__main__":
    subreddit = "unpopular"
    word_list = ['you', 'unpopular', 'vote', 'down', 'downvote', 'her', 'politics']
    count_words(subreddit, word_list)
