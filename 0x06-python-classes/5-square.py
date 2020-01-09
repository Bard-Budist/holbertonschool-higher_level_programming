#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        """
        docstring for __init__
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """docstring for fname"""
        return (self.__size * self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        """
            doscstring for area
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def my_print(self):
        """docstring for f"""
        x = self.__size
        if (x == 0):
            print()
        for i in range(x):
            for y in range(x):
                print("#", end="")
            print()
