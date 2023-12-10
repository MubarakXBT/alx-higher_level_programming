#!/usr/bin/python3
""" module json to encode to return JSON of a string"""
import json


def to_json_string(my_obj):
    """ A function to encode string to a json format
    Args:
        my_obj: a string object
    Return:
        JSON representation of the object (string)
    """
    return (json.dumps(my_obj))
