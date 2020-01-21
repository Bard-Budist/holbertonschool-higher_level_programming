#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return (vars(self))
        dic2 = {}
        dic = vars(self)
        for key, value in dic.items():
            if key in attrs:
                dic2[key] = value
        return dic2
