#!/usr/bin/python3
"""
    Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
        Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Init
        """
        self.__width = self.validationD(width, "width")
        self.__height = self.validationD(height, "height")
        self.__x = self.validationC(x, "x")
        self.__y = self.validationC(y, "y")
        super().__init__(id)

    @property
    def width(self):
        """
            width gettter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            width setter
        """
        self.__width = self.validationD(value, "width")

    @property
    def height(self):
        """
            height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            height setter
        """
        self.__height = self.validationD(value, "height")

    @property
    def x(self):
        """
            x gettter
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            x setter
        """
        self.__x = self.validationC(value, "x")

    @property
    def y(self):
        """
            t gettter
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            y setter
        """
        self.__y = self.validationC(value, "y")

    @staticmethod
    def validationD(value, name):
        """
            validation
        """
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        elif (value <= 0):
            raise ValueError("{} must be > 0".format(name))
        return value

    @staticmethod
    def validationC(value, name):
        """
            validation
        """
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        elif (value < 0):
            raise ValueError("{} must be >= 0".format(name))
        return value

    def area(self):
        """
            area
        """
        return (self.__width * self.__height)

    def display(self):
        """
            display
        """
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width, end="")
            print()

    def __str__(self):
        """
            str
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x
                , self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """
            update
        """
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
        """
            update
        """
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
        """
            To dictionary
        """
        return {'x': self.__x, 'y': self.__y, 'id': self.id
                , 'width': self.__width, 'height': self.__height}
