#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if(len(matrix) > 1):
        for row in matrix:
            row_content = []
            for i in range(len(row)):
                row_content.append(row[i])
            print("{} {} {}".format(row[0], row[1], row[2]))
    else:
        print()
