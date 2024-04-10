#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        'User-Agent': 'MyApp/0.1',
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return 0
    else:
        data = response.json()
        return data['data']['subscribers']
