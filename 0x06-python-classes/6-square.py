#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        """
        docstring for __init__
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if ((type(position) is not tuple)
                or (type(position[0]) is not int
                    or type(position[1]) is not int)
                or (position[0] < 0 or position[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):
        """
        Note:
            Rerturn position
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Note:
            Set value to Position
        Args:
            position (:obj: is a tuple)
        """
        if ((type(value) is not tuple)
                or (len(value) < 2)
                or (type(value[0]) is not int or type(value[1]) is not int)
                or (value[0] < 0 or value[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """docstring for f"""
        x = self.__size
        if (x == 0 or self.__position[1] > 0):
            print()
        for i in range(x):
            for item in range(self.position[0]):
                print(" ", end="")
            for y in range(x):
                print("#", end="")
            print()

    def area(self):
        """docstring for fname"""
        return (self.__size * self.__size)
