#!/usr/bin/python3
"""
Module 3-square
Defines class Square with private attribute size, size validation
and area calculation
"""


class Square:
    """
    A class representing a square.
    """

    def __init__(self, size=0):
        """
        Initialize a Square object with an optional size.

        Args:
            size (int): The size of the square. Defaults to 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate and return the current area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
