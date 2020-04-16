#!/usr/bin/python3
"""Task 04"""
import requests


if __name__ == "__main__":
    rp = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(rp.content.decode('utf-8'))))
    print("\t- content: {}".format(rp.content.decode('utf-8')))
