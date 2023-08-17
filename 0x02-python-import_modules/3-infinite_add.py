#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    count = len(argv) - 1
    i = 1
    add = 0
    while count > 0:
        add = add + int(argv[i])
        count -= 1
        i += 1
    print(add)
