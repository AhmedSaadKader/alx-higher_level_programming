#!/usr/bin/python3

def no_c(my_string):
    string_list = list(my_string)
    for c in string_list:
        if (c == 'c') | (c == 'C'):
            string_list.remove(c)
    new_string = ''.join(string_list)
    return new_string
