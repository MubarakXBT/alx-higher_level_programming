#!/usr/bin/python3
""" A module of class that invert equality operator"""


class MyInt(int):
    """
    """
    def __new__(cls, value):
        return (super().__new__(cls, value))

    def __eq__(self, other):
        return (not super().__eq__(other))

    def __ne__(seld, other):
        return (not super().__ne__(other))

