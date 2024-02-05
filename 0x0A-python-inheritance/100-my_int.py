#!/usr/bin/python3
"""MyInt class"""


class MyInt(int):
    """MyInt class extends int and reverses some operators

    Args:
        int (_type_): _description_
    """
    def __init__(self, value):
        self.value = value

    def __eq__(self, otherInt):
        return self.value != otherInt

    def __ne__(self, otherInt):
        return self.value == otherInt
