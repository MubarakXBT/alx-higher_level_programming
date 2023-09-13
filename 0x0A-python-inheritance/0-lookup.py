#!/usr/bin/python3
""" Module to return attribute of an object"""


def lookup(obj):
    """ Lookup - A function to return attribute of an object
    Args:
        obj (class): an instance of an object
    """
    return (dir(obj))
