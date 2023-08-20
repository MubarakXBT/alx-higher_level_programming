#!/usr/bin/python3
def uniq_add(my_list=[]):
    seq = set(my_list)
    res = 0
    for x in seq:
        res += x
    return (res)
