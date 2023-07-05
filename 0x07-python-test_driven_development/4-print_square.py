#!/usr/bin/python3


def print_square(size):
    """
    Prints a square with '#' characters of the given size.

    Args:
        size (int): The size of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        return

    square = "#" * size
    for _ in range(size):
        print(square)
