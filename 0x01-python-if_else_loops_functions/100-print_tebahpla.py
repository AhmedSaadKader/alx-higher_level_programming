#!/usr/bin/python3
def print_tebahpla():
    for i in range(-122, -96):
        if (abs(i) % 2 != 0):
            a = abs(i) - 32
        else:
            a = abs(i)
        print("{}".format(chr(a)), end="")


print_tebahpla()
