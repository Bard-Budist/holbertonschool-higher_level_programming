#!/usr/bin/python3
import urllib.request
import sys


if __name__ == "__main__":

    header = urllib.request.Request(sys.argv[1], method='GET')
    with urllib.request.urlopen(header) as resp:
        print(resp.headers.get('X-Request-Id'))