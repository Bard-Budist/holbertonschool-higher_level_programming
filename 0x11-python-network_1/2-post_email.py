#!/usr/bin/python3
"""Task 02"""
import urllib.request
import sys
import urllib.parse


if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(data)
    data = data.encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data, method='POST')
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
