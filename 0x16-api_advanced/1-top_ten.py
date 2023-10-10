#!/usr/bin/python3
"""function that queries Reddit API and prints
    titles of first 10 hot posts in subreddit"""

import requests


def top_ten(subreddit):
    """function queries reddit API and prints titles of first 10 posts"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'My user Agent 1.0'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
        else:
            print(None)
