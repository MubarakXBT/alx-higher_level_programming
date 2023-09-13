#!/usr/bin/python3
""" Module of class MyList that inherit from a superclass list"""


class MyList(list):
    """ a subclass of list"""
    pass

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
