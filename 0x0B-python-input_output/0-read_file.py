#!/usr/bin/python3
""" A module to open and read a file to STDOUT"""


def read_file(filename=""):
    """ reads file to stdout.
    Args:
        filename: name of the file, text is to be read from.
    Returns:
        Null.
    """
    with open(filename, mode="r", encoding="utf-8") as myfile:
        {
            print(myfile.read(), end="")
        }
