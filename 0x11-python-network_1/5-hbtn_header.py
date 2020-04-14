#!/usr/bin/python3
"""Task 05"""
import requests
import sys

if __name__ == "__main__":
    with  requests.get(sys.argv[1]) as rp:
        print(rp.headers.get('X-Request-Id'))