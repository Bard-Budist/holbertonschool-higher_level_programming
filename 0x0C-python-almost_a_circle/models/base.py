#!/usr/bin/python3
"""
    Base
    This is a base
"""
import json


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
                print(data)
                for item in data:
                    lists.append(cls.create(**item))
                return lists
        except IOError:
            return lists
