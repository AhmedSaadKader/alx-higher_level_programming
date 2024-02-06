#!/usr/bin/python3
"""a script that add all arguments to a python list"""
import sys
from pathlib import Path


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

file_name = "add_item.json"
file_path = Path(file_name)
my_list = []
if file_path.exists():
    my_list = load_from_json_file("add_item.json")
save_to_json_file(my_list + sys.argv[1:], "add_item.json")
