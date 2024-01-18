#!/usr/bin/python3
""" 17-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    r1 = Square(3, 5, 1)
    r1_dictionary = r1.to_dictionary()
    r2 = Rectangle.create(**{ 'size': 2, 'x': 1, 'y': 3 })
    print(r1)
    print(r2)
    print(r1 is r2)
    print(r1 == r2)