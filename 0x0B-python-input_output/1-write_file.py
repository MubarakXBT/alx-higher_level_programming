#!/usr/bin/python3
"""A module to write to file"""


def write_file(filename="", text=""):
    """ function to write to the file
    Args:
        @filename: file where text is to be stored
        @text: string to be inserted or appended to the file
    """
    with open(filename, mode="w", encoding="utf-8") as myfile:
        return(myfile.write(text))
