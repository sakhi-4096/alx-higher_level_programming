#!/usr/bin/python3


def add_integer(a, b=98):
    """
    Adds two values and returns the sum as an integer.

    Args:
        a (int or float): The first value.
        b (int or float, optional): The second value. Defaults to 98.
    Returns:
        int: The sum of the two values as an integer.
    Raises:
        TypeError: If either a or b is not an instance of int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    return int(a) + int(b)
