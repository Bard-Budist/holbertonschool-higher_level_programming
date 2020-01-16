#!/usr/bin/python3
class Rectangle():

    def __init__(self, width=0, height=0):
        self.__height = self.checkHeight(height)
        self.__width = self.checkWidth(width)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = self.checkHeight(value)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = self.checkWidth(value)

    @staticmethod
    def checkWidth(width):
        if (type(width) is not int):
            raise TypeError("width must be an integer")
        if (width < 0):
            raise ValueError("width must be >= 0")
        return width

    @staticmethod
    def checkHeight(height):
        if (type(height) is not int):
            raise TypeError("height must be an integer")
        if (height < 0):
            raise ValueError("height must be >= 0")
        return height
