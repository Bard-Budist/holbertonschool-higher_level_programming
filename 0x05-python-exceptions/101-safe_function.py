#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        resul = fct(args[0], args[1])
    except (IndexError, ZeroDivisionError, ValueError) as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None
    return resul
