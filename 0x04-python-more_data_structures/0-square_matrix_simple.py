#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix != []:
        new_matrix = []
        for column in range(len(matrix)):
            transposed_row = []
            for row in range(len(matrix[column])):
                transposed_row.append(matrix[column][row] ** 2)
            new_matrix.append(transposed_row)
        return (new_matrix)
