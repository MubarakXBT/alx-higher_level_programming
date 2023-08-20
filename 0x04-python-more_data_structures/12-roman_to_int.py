#!/usr/bin/python3
def roman_to_int(roman_string):
    lib = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string is None or not (isinstance(roman_string, str)):
        return (0)
    else:
        lst = []
        for name in roman_string:
            for k, v in lib.items():
                if name == k:
                    lst.append(v)
                    break
        lst.append(0)
        j = 1
        i = 0
        result = 0
        while i < len(lst):
            if j <= len(roman_string):
                if lst[i] < lst[j]:
                    result += lst[j] - lst[i]
                    i += 2
                    j += 2
                else:
                    result += lst[i]
                    j += 1
                    i += 1
            else:
                break
        return (result)
