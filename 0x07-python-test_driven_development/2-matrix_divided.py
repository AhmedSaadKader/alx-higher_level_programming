#!/usr/bin/python3

"""
This module contains one function matrix_divided() -

this function divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix
    """
    new_matrix = []
    for list in matrix:
        new_list = []
        for number in list:
            if type(number) not in [int, float]:
                raise TypeError("matrix must be all integers")
            new_list.append(round((number / div), 2))
        new_matrix.append(new_list)
    return new_matrix
