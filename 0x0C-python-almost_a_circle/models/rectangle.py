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
        self.__height = height
        self.__width = width
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self):
        return (self.__width)

    @width.getter
    def width(self):
        return (self.__width)

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self):
        return (self.__height)

    @height.getter
    def height(self):
        return (self.__height)

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def width(self):
        return (self.__x)

    @x.getter
    def width(self):
        return (self.__x)

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def width(self):
        return (self.__y)

    @y.getter
    def width(self):
        return (self.__y)
