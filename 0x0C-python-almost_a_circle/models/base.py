#!/usr/bin/python3
import json
#from base import Base


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if (id is None):
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        lists = []
        ban = 0
        print(len(list_objs[0].to_dictionary()))
        if list_objs is not None:
            #string = ("Rectangle" if isinstance(list_objs[0], Rentangle)
            #        else "Square")
            for check in list_objs:
                if (issubclass(type(check), Base) == False):
                    ban = 1
            if ban == 0:
                for items in list_objs:
                    print(items)
                    lists.append(cls.to_json_string([items.to_dictionary()]))
            file = open("Rectangle.json", mode="w+")
            file.write(str(lists))
            file.close
        return lists


