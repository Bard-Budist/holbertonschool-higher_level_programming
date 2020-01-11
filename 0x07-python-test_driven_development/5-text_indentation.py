#!/usr/bin/python3
def text_indentation(text):
    if (text != None):
        text = text.replace(".", ".\n\n")
        text = text.replace("?", "?\n\n")
        text = text.replace(":", ":\n\n")
        text = text.replace("\n\n ", "\n\n")
        print(text)