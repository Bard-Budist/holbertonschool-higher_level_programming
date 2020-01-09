#!/usr/bin/python3
class Square:
        """
        Square funtion
        Attributes:
                size (int): Size
        """

        def __init__(self, size=0):
            """
            Note:
                Inicializate function
            Args:
                size (:obj:`int`, optional): Size
             Attributes:
                size (int): Size
            """
            if (type(size) is not int):
                raise TypeError("size must be an integer")
            elif (size < 0):
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
