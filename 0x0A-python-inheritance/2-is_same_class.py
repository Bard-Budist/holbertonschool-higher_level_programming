#!/usr/bin/python3
def is_same_class(obj, a_class):
    if (obj != object and a_class == object):
        return False
    return (True if isinstance(obj, a_class) else False)