#!/usr/bin/python3
def uppercase(str):
    i = 0
    j = 97
    new_str = ""
    while i < len(str):
        if j != 123 and j != ord(str[i]):
            j = j + 1
            continue
        elif j < 123 and j == ord(str[i]):
            j = j - 32
            new_str = new_str + chr(j)
            j = 97
            i = i + 1
        elif j == 123:
            new_str = new_str + str[i]
            i = i + 1
            j = 97
    print("{}".format(new_str))
