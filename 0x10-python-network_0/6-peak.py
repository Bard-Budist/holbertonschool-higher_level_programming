#!/usr/bin/python3
"""Find peak"""
def find_peak(list_of_integers):
    """Find peak"""
    if len(list_of_integers) == 0:
        return None
    n = list_of_integers[0]
    for number in list_of_integers:
        if number > n:
            n = number
    return n