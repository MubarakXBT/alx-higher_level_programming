#!/usr/bin/python3
def no_c(my_string):
    new_string = ''
    for i in my_string:
        if i != 'C' or i != 'c':
            new_string += i
    return (my_string)
