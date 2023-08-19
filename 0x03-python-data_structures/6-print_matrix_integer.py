#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix != [[]]:
        for row in matrix:
            l = len(row)
            break
        for row in matrix:
            for i in range(l):
                if i == (l - 1):
                    print("{:d}".format(row[i]),end='')
                else:
                    print("{:d}".format(row[i]), end=' ')
            print("".format())
    else:
        print("".format())
