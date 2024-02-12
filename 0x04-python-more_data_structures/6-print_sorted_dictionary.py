#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_keys = ([k for k, v in a_dictionary.items()])
    sorted_keys.sort()
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
