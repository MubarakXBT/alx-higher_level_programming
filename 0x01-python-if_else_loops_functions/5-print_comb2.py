#!/usr/bin/python3
i = 0
j = 0
while i <= 9 and j <= 9:
    if i == 9 and j == 9:
        print("{}{}".format(i, j))
        break
    elif i <= 9 and j <= 9:
        print("{}{},".format(i, j), end=" ")
    if j == 9:
        i = i + 1
        j = 0
        continue
    j = j + 1
