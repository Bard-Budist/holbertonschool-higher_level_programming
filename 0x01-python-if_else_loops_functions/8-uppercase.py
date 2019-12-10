#!/usr/bin/python3
def uppercase(str):
    str = str + "\n"
    for i in str:
        code = ord(i)
        if i in "abcdefjhijklmnopqrstuvwxyz":
            code = ord(i) - 32
        print("{:c}".format(code), end='')
