#!/usr/bin/python3
""" a module for performs task on name"""


def say_my_name(first_name, last_name=""):
    """ say_my_name - A function to send name to STDOUT_FILENO
    Args:
        first_name (str): first name of the individual
        last_name (str): Last name of the individual
    Returns:
        prints the name to standard outut
    """

    if not isinstance(first_name, str) or first_name.isdigit():
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str) or last_name.isdigit():
        raise TypeError("last_name must be a string")
    else:
        print(first_name + ' ' + last_name)
