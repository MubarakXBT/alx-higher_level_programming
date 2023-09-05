#!/usr/bin/python3
""" contains functions that performs task on matrix"""


def matrix_divided(matrix, div):
    """ Function to Divide element in a list by a given divisor

    Args:
        matrix (list): A list of list representing an array
        div (int): a divisor that is greater than 0

    Returns:
        a divided list

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: div must be a number
        ZeroDivisionError: division by zero
    """

    message = "matrix must be a matrix (list of lists) of integers/floats"
    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if (not isinstance(matrix, list) or matrix is None):
        raise TypeError(message)
    elif (matrix == [] or matrix == [[]]):
        raise TypeError(message)
    for row in matrix:
        if isinstance(row, list):
            for x in row:
                if not isinstance(x, (int, float)):
                    raise TypeError(message)
        else:
            raise TypeError(message)

    for row in matrix:
        length_1 = len(row)
    for row in matrix:
        if len(row) != length_1:
            raise TypeError("Each row of the matrix must have the same size")
    transposed = [[round(float(x)/div, 2) for x in row] for row in matrix]
    return (transposed)
