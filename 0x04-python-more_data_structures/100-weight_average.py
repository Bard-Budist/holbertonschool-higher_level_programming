#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    num1, num2, band = 0, 0, 0
    for i in range(len(my_list)):
        num1 += my_list[i][0] * my_list[i][1]
        num2 += my_list[i][1]
    return num1 / num2
