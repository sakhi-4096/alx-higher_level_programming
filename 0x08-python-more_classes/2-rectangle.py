#!/usr/bin/python3
"""
Module 2-rectangle
Contains class rectangle with private instance attributes
and public instance method
"""


class Rectangle:
    """
    Represents a rectangle with a width and height,
    and provides methods to calculate its area and perimeter.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with the given width and height.
        """
        self.__width = 0
        self.__height = 0
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)
