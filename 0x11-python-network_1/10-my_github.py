#!/usr/bin/python3
"""Task 10"""
import requests
import sys

if __name__ == "__main__":
    data = {'Authorization': 'token ' + sys.argv[2]}
    user = sys.argv[1]
    rp = requests.get('https://api.github.com/users/' + user, data)
    print(rp.json().get('id'))