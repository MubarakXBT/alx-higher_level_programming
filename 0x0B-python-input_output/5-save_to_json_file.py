#!/usr/bin/python3
""" Module Json """
import json


def save_to_json_file(my_obj, filename):
    """ A function that Save json representation to a file
    Args:
        my_obj: string to be encoded to json
        filename: Name of file where the json representation is to be stored
    """
    with open(filename, mode="w", encoding="utf-8") as jsonfile:
        jsonfile.write(json.dumps(my_obj))
    jsonfile.closed
