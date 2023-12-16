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
        """ Saves the JSON string representation to a file
        Args:
            cls: class name
            list_objs: a list of instance who inherit base
        """
        filename = cls.__name__ + '.json'
        with open(filename, mode='w', encoding='utf-8') as myfile:
            if list_objs is None or list_objs == '[]':
                myfile.write('[]')
                return
            lis = [x.to_dictionary() for x in list_objs]
            f = Base.to_json_string(lis)
            myfile.write(f)

    @staticmethod
    def from_json_string(json_string):
        """Decode the JSON string
        Args:
            json_string: A json string representation
        Return:
            The list of JSON string representation
        """
        if json_string is None or len(json_string) == 0:
            return (list())
        mylist = json.loads(json_string)
        return (mylist)

    @classmethod
    def create(cls, **dictionary):
        """ Method that returns an insatance with all attributes
        Args:
            cls: class of the instance
            **dictionary: dictionary of attribute of instance
        Return:
            an instance with all attribute already set
        """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == 'Rectangle':
            dummy = Rectangle(width=3, height=2, id=2, x=3, y=1)
            dummy.update(**dictionary)
        else:
            dummy = Square(size=2, id=3, x=4, y=5)
            dummy.update(**dictionary)
        return dummy
