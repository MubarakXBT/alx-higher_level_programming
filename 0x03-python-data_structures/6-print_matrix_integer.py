#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix != [[]]:
        for row in matrix:
            for i in range(3):
                print("{}".format(row[i]), end=' ')
            print("".format())
    else:
        print("".format())