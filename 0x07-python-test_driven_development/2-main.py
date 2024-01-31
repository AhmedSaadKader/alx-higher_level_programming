#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
try:
    print(matrix_divided(matrix, 3))
    print(matrix_divided(matrix, 0))
    print(matrix)
except Exception as e:
    print('zero division: ', e)

try:
    matrix = ""
    print(matrix_divided(matrix, 3))
except Exception as e:
    print("not a list: ", e)

try:
    matrix = []
    print(matrix_divided(matrix, 3))
except Exception as e:
    print("empty list: ", e)

try:
    matrix = ["s"]
    print(matrix_divided(matrix, 3))
except Exception as e:
    print("list of strings: ", e)

try:
    matrix = [[2, 3, 4], [2, 3]]
    print(matrix_divided(matrix, 3))
except Exception as e:
    print("different sized rows: ", e)

try:
    matrix = [[2, 3], [2, 3]]
    print(matrix_divided(matrix, float("inf")))
except Exception as e:
    print("different sized rows: ", e)
