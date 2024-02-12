#!/usr/bin/python3
for i in range(0, 10):
    if i == 8:
        for n in range(i + 1, 10):
            if n == 9:
                print("{}{}".format(i, n))
    else:
        for n in range(i + 1, 10):
            print("{}{}".format(i, n), end=", ")
