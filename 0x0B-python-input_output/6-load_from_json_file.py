#!/usr/bin/python3
""" Module JSON """
import json


def load_from_json_file(filename):
    """ A function to decode json from a file
    Args:
        filename: JSON file that contains the representation
    Return:
        an Object from the JSON file
    """
    with open(filename, mode="r+", encoding="utf-8") as jsonfile:
        return (json.loads(jsonfile.read()))
