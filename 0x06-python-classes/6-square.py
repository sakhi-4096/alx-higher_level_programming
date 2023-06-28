#!/usr/bin/python3
"""
Module 6-square
Defines class Square with private attributes and public methods
"""


class Square:
    """
    A class representing a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a Square object with an optional size and position.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of the square. Defaults to (0, 0).
        Raises:
            TypeError: If size is not an integer of position is not a tuple
                        of 2 positive integers.
            ValueError: If size or position values are less than 0.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieve the current position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple): The position to set.
        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
            ValueError: If value contains negative values.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        x, y = value

        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise ValueError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Calculate and return the current area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the character #.

        Prints the square representation to stdout.
        If size is equal to 0, an empty line is printed.
        The position is used to determine the starting point of the square.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print("")

            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
