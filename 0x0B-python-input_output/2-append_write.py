#!/usr/bin/python3
""" A module to append to text file"""


def append_write(filename="", text=""):
    """ A function to append to an already existing text file
    Args:
        filename: File that contains the texts
        text: the new set of text to be appended to the file
    Return:
        number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as myfile:
        return (myfile.write(text))
