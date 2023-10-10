#!/usr/bin/python3
"""function that queries Reddit API and prints
    titles of first 10 hot posts in subreddit"""

import requests


def top_ten(subreddit):
    """function queries reddit API and prints titles of first 10 posts"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'My user Agent 1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False)
        if response.status_code == 200:
            children = response.json().get('data').get('children')
            for i in range(10):
                print(children[i].get('data').get('title'))
        else:
            print("None")
    except Exception:
        print("None")
