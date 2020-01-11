#!/usr/bin/python3
import test

def add_integer(a, b=98):
    a = (int(a) if type(a) is float else a)
    b = (int(b) if type(b) is float else b)
    if (type(a) is not int):
        raise TypeError("a must be an integer")
    elif (type(b) is not int):
        raise TypeError("b must be an integer")
    return (a + b)