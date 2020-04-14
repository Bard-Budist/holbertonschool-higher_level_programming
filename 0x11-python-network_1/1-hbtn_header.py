#!/usr/bin/python3
import urllib.request
import sys
if __name__ == "__main__":
    values = {'q' : 'python programming tutorials'}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8') # data should be byte
    with urllib.request.Request('https://intranet.hbtn.io/status', data) as header:
       resp = urllib.request.urlopen(header)
       print(resp)
