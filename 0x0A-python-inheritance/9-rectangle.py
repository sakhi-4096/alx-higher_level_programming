#!/usr/bin/python3
"""
Module 9-rectangle
Contains parent class BaseGeometry
with public instance method area and integer_validation

Contains subclass Rectangle
with instantiation of private attributes width and height, validated by parent,
extends parent's area method and prints with __str__
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Inherits from BaseGeometry
    Methods:
        __init__(self, width, height)
        area(self)
        __str__
    """
    def __init__(self, width, height):
        """ Validate and initialize width and height
        Args:
            width (int): private
            height (int): private
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Extends parent's empty method and returns area """
        return self.__width * self.__height

    def __str__(self):
        """ Prints [Rectangle] <width>/<height> """
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__width, self.__height)
