#!/usr/bin/python3
class Rectangle():

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__height = self.checkHeight(height)
        self.__width = self.checkWidth(width)
        Rectangle.number_of_instances += 1
        Rectangle.print_symbol = Rectangle.print_symbol

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if (isinstance(rect_1, Rectangle) is False):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif (isinstance(rect_2, Rectangle) is False):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if (rect_1.area() == rect_2.area()):
            return rect_1
        elif (rect_1.area() > rect_2.area()):
            return rect_1
        else:
            rect_2

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if (self.__height == 0 or self.__width == 0):
            return 0
        else:
            return (2 * (self.__height + self.__width))

    def __str__(self):
        string = ""
        if (self.__height == 0 or self.__width == 0):
            return ""
        else:
            for x in range(self.__height):
                for y in range(self.__width):
                    string += "%s" % ((self.print_symbol))
                string += ("\n" if x + 1 != self.__height else "")
        return string

    def __repr__(self):
        string = "Rectangle" + str(eval('self.width, self.height'))
        return string

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
