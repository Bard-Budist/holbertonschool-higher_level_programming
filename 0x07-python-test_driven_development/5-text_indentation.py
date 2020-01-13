#!/usr/bin/python3
def text_indentation(text):
    if (text != None):
        c2 = 1
        for c in range(len(text)):
            if (text[c] == '?' or text[c] == ':' or text[c] == '.'):
                print("\n")
                while (text[c + c2] == ' '):
                    c2 += 1
                c = c + c2
                print(text[c], end="")