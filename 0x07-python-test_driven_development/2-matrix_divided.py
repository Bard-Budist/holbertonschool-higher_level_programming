#!/usr/bin/python3
"""
    function that divides all elements of a matrix.
    Args:
    Matix and div
"""
def matrix_divided(matrix, div):
    """
        function that divides all elements of a matrix
    """
    list2 = []
    lenl = 0
    if (type(div) is not int and type(div) is not float):
        raise TypeError("div must be a number")
    elif (isinstance(matrix[0], list) == False):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif (div == 0):
        raise ZeroDivisionError("division by zero")

    for i in range(len(matrix)):
        sublist = []
        for y in range(len(matrix[i])):
            if (type(matrix[i][y]) is not int and type(matrix[i][y]) is not float):
                raise TypeError("""\
            matrix must be a matrix (list of lists) of integers/floats\
            """)
            sublist.append(round(matrix[i][y] / div, 2))
        list2.append(sublist)
        if (lenl != y and lenl != 0):
            raise TypeError("Each row of the matrix must have the same size")
        lenl  = y


    return list2
