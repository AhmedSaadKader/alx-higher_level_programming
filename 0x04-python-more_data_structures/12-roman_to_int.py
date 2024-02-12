#!/usr/bin/python3

def roman_to_int(roman_string):
    int = 0
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman_value = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    for ind in range(len(roman_string)):
        value = roman_value[roman_string[ind]]
        if ind + 1 < len(roman_string):
            next_value = roman_value[roman_string[ind + 1]]
            if next_value > value:
                int -= value
            else:
                int += value
        else:
            int += value

    return int
