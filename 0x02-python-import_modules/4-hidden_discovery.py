#!/usr/bin/python3
import sys
import hidden_4 as hidden


def hidden_discovery():
    names = dir(hidden)
    for name in names:
        if not name.startswith("__"):
            print(name)


if __name__ == "__main__":
    hidden_discovery()
