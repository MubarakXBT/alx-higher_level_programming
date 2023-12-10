#!usr/bin/python3
import json
""" A Module to return Json of a string """


def to_json_string(my_obj):
    """ A function to encode string to a json format
    Args:
        my_obj: a string object
    Return:
        JSON representation of the object (string)
    """
    return (json.dumps(my_obj))
