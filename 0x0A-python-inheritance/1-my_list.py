#!/usr/bin/python3
""" Module of class MyList that inherit from a superclass list"""


class MyList(list):
    """ a subclass of list"""
    def __init__(self):
        """initialize the object"""
        list.__init__(self)

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
