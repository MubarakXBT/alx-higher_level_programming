#!/usr/bin/python3
"""
None
"""
import json


class Base:
    """
    Class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class instantation """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ JSON converter"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + '.json'
        with open(filename, mode='w', encoding='utf-8') as myfile:
            if list_objs is None or list_objs == '[]':
                myfile.write('[]')
                return
            lis = [x.to_dictionary() for x in list_objs]
            f = Base.to_json_string(lis)
            myfile.write(f)
