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
            __init__

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
        Return area
        Returns:
            Area :D
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """
        Getter size
        Return:
            Size
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Note:
            Get sizeda
        Args:
            size (:obj: 'int', optional)
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
