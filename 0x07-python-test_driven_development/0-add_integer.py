#!/usr/bin/python3
def add_integer(a, b=98):
    """ add_integer - a function that adds integers

    Args:
        a (int) = first number
        b (int) = second number

    Returns:
        added result of the numbers
    """
    if (not isinstance(a, float) and not isinstance(a, int)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, float) and not isinstance(b, int)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
