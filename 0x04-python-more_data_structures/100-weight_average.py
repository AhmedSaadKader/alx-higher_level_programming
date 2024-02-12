#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list is None or not my_list:
        return 0
    weight = 0
    score = 0
    for t in my_list:
        weight += t[1]
        score += t[0] * t[1]
    return score / weight
