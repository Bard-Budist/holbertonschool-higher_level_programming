#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 0
    if len(sys.argv) != 2:
        print("{:d} arguments:".format(len(sys.argv) - 1))
        for i in range(len(sys.argv)):
            if i != 0:
                print("{:d}: {}".format(i, sys.argv[i]))
    elif len(sys.argv) == 2:
        print("{:d} argument:".format(len(sys.argv) - 1))
        print("{:d}: {}".format(1 ,sys.argv[1]))
    else:
        print("{:d} arguments.".format(len(sys.argv) - 1))
