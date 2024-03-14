#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics
"""
import sys


stdin_size = 0
line_count = 0
for line in sys.stdin:
    if line_count != 0 and line_count % 10 == 0:
        print(stdin_size)
    line_count += 1
    line_len = len(line)
    stdin_size += line_len
    print(line, end='')
