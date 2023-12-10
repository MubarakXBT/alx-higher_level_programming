#!/usr/bin/python3
""" module json to decode returning  object of a JSON string """
import json


def from_json_string(my_str):
    """ A function to decodes json format to string
    Args:
        my_str: a JSON string
    Return:
        object representation of the JSON (string)
    """
    return (json.loads(my_str))
