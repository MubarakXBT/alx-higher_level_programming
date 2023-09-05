#!/usr/bin/python3
""" Define  Class Square"""


class Square:
    """Represent sqaure"""

    def __init__(self, size=0, position=(0, 0)):
        """ initialization of Square size
        Args:
            size (int): size of new square.
            position (tuple): positioning of the square to stdout
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ set position """
        return (self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ returns area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """prints the Square using '#' """
        if self.__size == 0:
            print()
        else:
            [print() for i in range(self.__position[1])]
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
