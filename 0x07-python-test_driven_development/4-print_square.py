#!/usr/bin/python3
""" Contains function that handles a square"""


def print_square(size):
    """ print_square - A function that prints square
    Args:
        size (int): Size length of the square
    Return:
        prints the square using giving size
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if size == 0:
        print()
        return

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
