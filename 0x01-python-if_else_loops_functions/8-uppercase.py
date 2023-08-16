#!/usr/bin/python3
def uppercase(str):
    i = 0
    j = 97
    while i < len(str):
        if j != 123 and j != ord(str[i]):
            j = j + 1
            continue
        elif j < 123 and j == ord(str[i]):
            j = j - 32
            print("{:c}".format(j), end="")
            j == 97
            i = i + 1
        elif j == 123:
            print("{}".format(str[i]), end="")
            i = i + 1
            j = 97
    print()
