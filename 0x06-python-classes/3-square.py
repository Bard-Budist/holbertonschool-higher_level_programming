#!/usr/bin/python3
class Square:
    """
    Function Square

    Attributes:
        size (:obj:`int`, optional): Size square

    """

    def __init__(self, size=0):
        """
        Note:
            Inicializce Function
        Args:
            size (:obj:`int`, optional): Size square
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Function to square

        Returns:
            Square
        """
        return (self.__size * self.__size)
