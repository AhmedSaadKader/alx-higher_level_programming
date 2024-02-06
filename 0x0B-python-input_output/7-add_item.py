#!/usr/bin/python3
"""a script that add all arguments to a python list"""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

    file_name = "add_item.json"
    my_list = load_from_json_file(file_name)
    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, file_name)
