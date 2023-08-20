#!/usr/bin/python3
def best_score(a_dictionary):
    i = 0
    if a_dictionary is None or len(a_dictionary) == 0:
        return (None)
    for k, v in a_dictionary.items():
        if v > i:
            i = v
            j = k
    return (j)
