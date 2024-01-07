#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    sum_1 = 0
    sum_2 = 0
    if len(tuple_b) > 1 and len(tuple_a) > 1:
        sum_1 = tuple_a[0] + tuple_b[0]
        sum_2 = tuple_a[1] + tuple_b[1]
    if len(tuple_b) == 1 and len(tuple_a) == 1:
        sum_1 = tuple_a[0] + tuple_b[0]
        return (sum_1, 0)
    if len(tuple_b) == 0 and len(tuple_a) == 0:
        return (0, 0)
    elif len(tuple_a) == 1:
        sum_1 = tuple_a[0] + tuple_b[0]
        sum_2 = 0 + tuple_b[1]
    elif len(tuple_a) == 0:
        sum_1 = 0 + tuple_b[0]
        sum_2 = 0 + tuple_b[1]
    elif len(tuple_b) == 1:
        sum_1 = tuple_a[0] + tuple_b[0]
        sum_2 = tuple_a[1] + 0
    elif len(tuple_b) == 0:
        sum_1 = tuple_a[0] + 0
        sum_2 = tuple_a[1] + 0
    return (sum_1, sum_2)
