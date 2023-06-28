#!/usr/bin/python3
"""
Module 4-square
Defines class Square with private size and public area
Can access and update size
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
        self.size = size

    @property
    def size(self):
        """
        Retrieve the current size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size to set.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the current area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
