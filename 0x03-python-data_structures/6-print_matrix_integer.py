#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix != [[]]:
        for row in matrix:
            for i in range(3):
                if i == 2:
                    print("{:d}".format(row[i]),end='')
                else:
                    print("{:d}".format(row[i]), end=' ')
            print("".format())
    else:
        print("".format())
