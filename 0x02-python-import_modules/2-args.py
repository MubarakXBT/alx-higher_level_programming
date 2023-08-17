#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    count = len(argv)
    if count == 1:
        print((count - 1), "arguments.")
    else:
        count -= 1
        if count > 1:
            print(count, "arguments:")
        else:
            print(count, "argument:")
        i = 1
        while count > 0:
            print("{}: {}".format(i, argv[i]))
            count -= 1
            i += 1
