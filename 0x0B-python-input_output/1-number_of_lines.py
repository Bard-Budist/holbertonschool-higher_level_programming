#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, mode="r") as file:
        Clines = 0
        for lines in file:
            Clines += 1
        return Clines
    return 0
