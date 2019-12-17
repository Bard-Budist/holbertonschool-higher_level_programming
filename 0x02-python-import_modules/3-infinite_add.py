#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    all = 0
    for item in range(len(sys.argv) - 1):
        all += int(sys.argv[item + 1])
    print("{:d}".format(all))
