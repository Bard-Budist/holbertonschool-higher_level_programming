#!/usr/bin/python3
import urllib.request
if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as rp:
        body = rp.read()
        print(
            """Body response:\n
            \t- type: {}\n
            \t- content: {}\n
            \t- utf8 content: {}""".format(type(body), body, "OK"))
