#!/usr/bin/python3
"""Task 07"""
import requests
import sys


if __name__ == "__main__":
    rp = requests.get(sys.argv[1])
    if rp.status_code >= 400:
        print("Error code: {:d}".format(rp.status_code))
    else:
        print(rp.content.decode('utf-8'))
