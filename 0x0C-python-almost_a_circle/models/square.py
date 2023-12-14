#!/usr/bin/python3
""" module parent base"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.size))

    @property
    def size(self):
        """getter for size"""
        return self.__width

    @size.setter
    def size(self, value):
        self.__width = value
        self.__height = value
