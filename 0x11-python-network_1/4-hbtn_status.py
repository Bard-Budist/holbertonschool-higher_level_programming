#!/usr/bin/python3
"""Task 04"""
import requests


if __name__ == "__main__":
    with requests.get('https://intranet.hbtn.io/status') as rp:
        print("Body response:\n\t - type: {}\n\t - content: {}".format(
                type(rp.content.decode('utf-8')),
                rp.content.decode('utf-8')))
