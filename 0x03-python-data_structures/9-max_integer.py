#!/usr/bin/python3
def max_integer(my_list=[]):
    num = 0
    if not my_list:
        return None
    for item in my_list:
        if item > num:
            num = item
    return num
