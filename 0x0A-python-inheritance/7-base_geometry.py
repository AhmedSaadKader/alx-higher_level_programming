#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """Basic Geometry class

    Parameters
    ----------

    Raises
    ------
    """

    def area(self):
        """Calculates area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the integer

        Parameters
        ----------
        name: a string describing the value
        value: the value of the name

        Raises
        ------
        TypeError
            Raised when value is not an integer
        ValueError
            Raised when value is not greater than 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
