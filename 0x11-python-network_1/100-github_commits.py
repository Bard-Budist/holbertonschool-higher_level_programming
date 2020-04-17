#!/usr/bin/python3
"""Task 100"""
import requests
import sys

if __name__ == "__main__":
    cont = 0
    repo = sys.argv[1]
    own = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        own,
        repo)

    rp = requests.get(url)
    commit = rp.json()

    for i in commit:
        if (cont == 10 or cont == len(commit)):
            break
        print("{}: {}".format(
            i.get('sha'),
            i.get('commit').get('author').get('name')))
        cont = cont + 1
