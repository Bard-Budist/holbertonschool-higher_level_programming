#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    roman_Char = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    roman = [1, 5, 10, 50, 100, 500, 1000]
    romansum = 0
    temp = 0
    letter = ''
    for iR in range(len(roman_string)):
        letter = roman_string[iR]
        for jR in range(len(roman_Char)):
            if letter == roman_Char[jR]:
                romansum += roman[jR]
                if temp < roman[jR]:
                    romansum -= temp * 2
                    temp = roman[jR]
                else:
                    temp = roman[jR]
    return romansum
