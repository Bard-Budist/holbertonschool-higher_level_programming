#!/usr/bin/python3
"""Task 03"""
import sys
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(request) as rp:
            print(rp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {:d}".format(e.code))
