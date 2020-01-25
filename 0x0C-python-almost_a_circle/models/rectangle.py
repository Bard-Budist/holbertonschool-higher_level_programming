#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = self.validationD(width, "width")
        self.__height = self.validationD(height, "height")
        self.__x = self.validationC(x, "x")
        self.__y = self.validationC(y, "y")
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = self.validationD(value, "width")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = self.validationD(value, "height")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = self.validationC(value, "x")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = self.validationC(value, "y")

    @staticmethod
    def validationD(value, name):
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        elif (value <= 0):
            raise ValueError("{} must be > 0".format(name))
        return value

    @staticmethod
    def validationC(value, name):
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        elif (value < 0):
            raise ValueError("{} must be >= 0".format(name))
        return value

    def area(self):
        return (self.__width * self.__height)

    def display(self):
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width, end="")
            print()

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x
                , self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        if (len(args) != 0 and args is not None):
            tam = len(args)
            if (tam >= 1):
                self.id = args[0]
            if (tam >= 2):
                self.__width = self.validationD(args[1], "width")
            if (tam >= 3):
                self.__height = self.validationD(args[2], "height")
            if (tam >= 4):
                self.__x = self.validationC(args[3], "x")
            if (tam >= 5):
                self.__y = self.validationC(args[4], "y")
        else:
            self.validateUpdate(args, kwargs)

    def validateUpdate(self, args, kwargs):
        if ("id" in kwargs):
            self.id = kwargs["id"]
        if ("width" in kwargs):
            self.__width = self.validationD(kwargs["width"], "width")
        if ("height" in kwargs):
            self.__height = self.validationD(kwargs["height"], "height")
        if ("x" in kwargs):
            self.__x = self.validationC(kwargs["x"], "x")
        if ("y" in kwargs):
            self.__y = self.validationC(kwargs["y"], "y")

    def to_dictionary(self):
        return {'x': self.__x, 'y': self.__y, 'id': self.id
                , 'width': self.__width, 'height': self.__height}






