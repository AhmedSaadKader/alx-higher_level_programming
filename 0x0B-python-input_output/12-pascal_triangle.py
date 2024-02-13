#!/usr/bin/python3
"""returns a list of lists of integers representing the Pascal's 
triangle of n
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal's 
    triangle of n

    Args:
        n (int): number
    """
    if n <= 0:
        return []
    pascal_list = [[1]]
    for _ in range(1, n):
        prev_row = pascal_list[-1]
        new_row = [1]
        for i in range(1, len(prev_row)):
            new_row.append(prev_row[i-1] + prev_row[i])
        new_row.append(1)
        pascal_list.append(new_row)
    return pascal_list
