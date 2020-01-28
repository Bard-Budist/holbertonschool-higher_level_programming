#!/usr/bin/python3
"""
    Base
    This is a base
"""
import json
import turtle


class Base:
    """
        Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            Init
        """
        if (id is None):
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            To_json_String
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Save to file
        """
        lists = []
        string = cls.__name__ + ".json"
        with open(string, mode="w+", encoding="utf-8") as f:
            if list_objs is not None:
                for items in list_objs:
                    lists.append(items.to_dictionary())
            f.write(cls.to_json_string(lists))

    @staticmethod
    def from_json_string(json_string):
        """
            From json
        """
        lists = []
        if (json_string is None or len(json_string) == 0):
            return lists
        return list(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
            create
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """
            load
        """
        string = cls.__name__ + ".json"
        lists = []
        try:
            with open(string, mode="r") as f:
                read = f.read()
                data = cls.from_json_string(read)
                for item in data:
                    lists.append(cls.create(**item))
                return lists
        except IOError:
            return lists

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
            save
        """
        lists = []
        string = cls.__name__ + ".csv"
        with open(string, mode="w+", encoding="utf-8") as f:
            if list_objs is not None:
                for item in list_objs:
                    lists.append(item.to_dictionary())
            f.write(cls.to_json_string(lists))

    @classmethod
    def load_from_file_csv(cls):
        """
            load
        """
        string = cls.__name__ + ".csv"
        lists = []
        try:
            with open(string, mode="r") as f:
                read = f.read()
                data = cls.from_json_string(read)
                for item in data:
                    lists.append(cls.create(**item))
                return lists
        except IOError:
            return lists

    @staticmethod
    def draw(list_rectangles, list_squares):
        x = 0
        colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
        rec = turtle.Turtle()
        rec.shape('turtle')
        if list_rectangles is not None:
            for itemsR in list_rectangles:
                rec.pencolor(colors[x%6])
                rec.penup()
                rec.setx(itemsR.x)
                rec.sety(itemsR.y)
                rec.pendown()
                for i in range(2):
                    rec.forward(itemsR.width)
                    rec.right(90)
                    rec.forward(itemsR.height)
                    rec.right(90)
                x += 1
        turtle.clearscreen()
        x = 0
        if list_squares is not None:
            rec = turtle.Turtle()
            rec.shape('turtle')
            for itemsQ in list_squares:
                rec.pencolor(colors[x%6])
                rec.penup()
                x = itemsQ.x
                y = itemsQ.y
                rec.setx(x)
                rec.sety(y)
                rec.pendown()
                for i in range(4):
                    rec.forward(itemsQ.size)
                    rec.right(90)
                x += 1
        turtle.exitonclick()
