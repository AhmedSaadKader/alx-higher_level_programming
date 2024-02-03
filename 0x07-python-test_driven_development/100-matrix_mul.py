#!/usr/bin/python3
"""
Module that contains function matrix mul

matrix_mul multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    matrix_mul multiplies 2 matrices
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
    col_b = []
    result = []
    for i in range(len(m_b[0])):
        inner_list = []
        for row in m_b:
            if not isinstance(row, list):
                raise TypeError("m_b must be a list of lists")
            inner_list.append(row[i])
        col_b.append(inner_list)

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        row_first = row[0]
        if not isinstance(row_first, (int, float)):
            raise TypeError("m_a should contain only integers or floats")
        row_second = row[1]
        if type(row_second) not in [int, float]:
            raise TypeError("m_a should contain only integers or floats")
        inner_result = []
        for col_no in range(len(m_b)):
            if type(col_b[col_no][0]) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
            result_first = row_first * col_b[col_no][0]
            if type(col_b[col_no][1]) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
            result_second = row_second * col_b[col_no][1]
            inner_result.append(result_first + result_second)
        result.append(inner_result)
    return (result)


if __name__ == "__main__":
    matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
