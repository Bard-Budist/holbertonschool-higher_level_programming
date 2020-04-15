#!/usr/bin/python3
"""Task 05"""
import requests
import sys

if __name__ == "__main__":
    rp = requests.get(sys.argv[1])
    print(rp.headers.get('X-Request-Id'))
