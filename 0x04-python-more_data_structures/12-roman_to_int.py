#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    romansum = 0
    for i in range(len(roman_string)):
        for key, value in roman.items():
            if roman_string[i] == key:
                romansum += value
    return romansum
