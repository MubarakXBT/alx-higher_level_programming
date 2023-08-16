#!/usr/bin/python3
i = 122
count = 0
while i >=  97:
    if count % 2 == 0:
        pr = i
    else:
        pr = i - 32
    print("{:c}".format(pr), end="")
    i = i - 1
    count = count + 1
