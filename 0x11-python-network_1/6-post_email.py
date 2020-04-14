#!/usr/bin/python3
"""Task 06"""
import requests
import sys


if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    rp = requests.post(sys.argv[1], data=data)
    print(rp.content.decode('utf-8'))
