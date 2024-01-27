#!/usr/bin/python3

"""
This module contains one function matrix_divided() -

this function divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix
    """
    if div == 0:
        raise ZeroDivisionError(
            "division by zero")
    if type(div) not in [int, float]:
        raise TypeError(
            "div must be a number")
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    row_len = len(matrix[0])
    new_matrix = []
    for row in matrix:
        if type(row) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        new_list = []
        for number in row:
            if type(number) not in [int, float]:
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats"
                    )
            new_list.append(round((number / div), 2))
        new_matrix.append(new_list)
    return new_matrix
