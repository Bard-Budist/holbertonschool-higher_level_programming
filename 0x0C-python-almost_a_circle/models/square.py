#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        s = "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y
                , self.width)
        return s

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value

    def update(self, *args, **kwargs):
        if (len(args) != 0 and args is not None):
            tam = len(args)
            if (tam >= 1):
                self.id = args[0]
            if (tam >= 2):
                self.width = args[1]
            if (tam >= 3):
                self.x = args[2]
            if (tam >= 4):
                self.y = args[3]
        else:
            self.validateUpdate(args, kwargs)

    def validateUpdate(self, args, kwargs):
        if ("id" in kwargs):
            self.id = kwargs["id"]
        if ("size" in kwargs):
            self.width = kwargs["size"]
        if ("x" in kwargs):
            self.x = kwargs["x"]
        if ("y" in kwargs):
            self.y = kwargs["y"]

    def to_dictionary(self):
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y':self.y}
