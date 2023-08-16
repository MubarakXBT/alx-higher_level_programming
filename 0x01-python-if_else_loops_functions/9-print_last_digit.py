#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        value = number % 10
    else:
        number = number * -1
        value = number % 10
    print(value, end="")
    return (value)
