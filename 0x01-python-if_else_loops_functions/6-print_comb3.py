#!/usr/bin/python3
n = 1
for i in range(0, 8):
    for c in range(n, 10):
        print("{:d}{:d}".format(i, c), end=", ")
    n = n + 1
print("89")
