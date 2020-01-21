#!/usr/bin/pythn3
def read_lines(filename="", nb_lines=0):
    with open(filename, mode="r", encoding="utf-8") as file: 
        nLines = 0
        for items in file:
            if (nLines == nb_lines and nb_lines != 0):
                break
            print(items, end="")
            if (nb_lines <= 0):
                continue
            nLines += 1
