#!/usr/bin/python3
def print_square(size):
    if (type(size) is float and size < 0) or (type(size) is not int):
        raise TypeError("size must be an integer")
    elif (size < 0):
        raise ValueError("size must be >= 0")

    for item in range(size):
        for i in range(size):
            print('#', end="")
        print()