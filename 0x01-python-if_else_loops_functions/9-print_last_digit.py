#!/bin/usr/python3
def print_last_digit(number):
    if number >= 0:
        return (number % 10)
    else:
        number = number * -1
        return (number % 10)