#!/usr/bin/python3
"""
Parent class - Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Object instantation"""
        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def width(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def width(self, value):
        self.__y = value
