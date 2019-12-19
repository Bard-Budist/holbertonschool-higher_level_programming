#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        new = {key: value}
        a_dictionary.update(new)
    else:
        a_dictionary[key] = value
    return a_dictionary
