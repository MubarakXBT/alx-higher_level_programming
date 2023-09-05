#!/usr/bin/python3
""" Define  Class Square"""


class Square:
    """Represent sqaure"""

    def __init__(self, size=0):
        """ initialization of Square size
        Args:
            size (int): size of new square.
        """
        self.__size = size

    @property
    def size(self):
        """ Get or set size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ returns area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """prints the Square using '#' """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
