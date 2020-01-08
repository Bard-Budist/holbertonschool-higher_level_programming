#!/usr/bin/python3
def safe_print_division(a, b):
    resul = None
    try:
        resul = a / b
    except ZeroDivisionError:
        pass
    finally:
        if resul is not None:
            print("Inside result: {:.1f}".format(resul))
        else:
            print("Inside result: {}".format(resul))
    return resul
