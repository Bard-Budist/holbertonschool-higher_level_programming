#!/usr/bin/python3
def uniq_add(my_list=[]):
    suma, var = 0, 0
    for item in range(len(my_list)):
        if not my_list[item] in my_list[:item]:
            suma += my_list[item]
    return suma
