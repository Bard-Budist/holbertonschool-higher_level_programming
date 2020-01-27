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
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Save to file
        """
        lists = []
        if list_objs is not None:
            string = cls.__name__ + ".json"
            for items in list_objs:
                lists.append(items.to_dictionary())
            file = open(string, mode="w+")
            file.write(str(lists))
            file.close
        return lists

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
        new = cls(5, 5)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """
            load
        """
        string = cls.__name__ + ".json"
        lists = []
        with open(string, "r") as file:
            dic = file.readlines()
            temp = str(dic[0])
            print(Base.from_json_string(temp))
            print(Base.from_json_string(dic[0]))
            for item in range(len(dic)):
                new = cls(5, 5)
                new.update(dic[item])
                lists.append(new)
        return lists
