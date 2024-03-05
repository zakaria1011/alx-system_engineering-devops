#!/usr/bin/python3
"""
task 0
"""
import requests


def number_of_subscribers(subreddit):
    if subreddit is None or type(subreddit) is not str:
        return 0

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': '0x16-api_advanced_project'}
    response = requests.get(url, headers=headers, allow_redirects=False).json()

    if response.get('data') is None:
        return 0

    subscribers = response.get('data').get('subscribers')
    return subscribers