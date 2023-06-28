#!/usr/bin/python3
"""
Module 1-square
Defines class Square with private attribute size
"""


class Square:
    """
    A class representing a square.
    """

    def __init__(self, size):
        """
        Initialize a Square object with a given size.

        Args:
            size: The size of the square.
        """
        self.__size = size
