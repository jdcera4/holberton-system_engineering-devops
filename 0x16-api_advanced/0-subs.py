#!/usr/bin/python3
"""
suscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    """
    try:
        rq = requests.get('https://www.reddit.com/r/{}/about.json'.
                          format(subreddit),
                          headers={'User-Agent': 'custom'},
                          allow_redirects=False)
        return rq.json().get('data').get('subscribers')
    except:
        return 0
