#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if (number >= 0):
    mod = number % 10
    if mod > 5:
        print(f"Last digit of {number} is {mod} and is greater than 5")
    elif mod == 0:
        print("Last digit of {} is {} and is 0".format(number, mod))
    else:
        print(f"Last digit of {number} is {mod} and is less than 6 and not 0")
else:
    num = number * -1
    mod = num % 10
    print(f"Last digit of {number} is -{mod} and is less than 6 and not 0")
