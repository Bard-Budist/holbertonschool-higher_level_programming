#!/usr/bin/python3
"""Task 100"""
import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    own = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        own,
        repo)

    rp = requests.get(url)
    commit = rp.json()
    for i in range(1, 10):
        dic = commit[i]
        print("{}: {}".format(dic.get('sha'), dic.get('author').get('login')))