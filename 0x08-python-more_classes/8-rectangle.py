#!/usr/bin/python3
"""
Contains class rectangle with private instance attributes and
public instance methods, string representation and instance
deletion and public class attributes and compare rectangles
"""


class Rectangle:
    """
    Represents a rectangle with a width and height,
    and provides methods to calculate its area and perimeter.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with the given width and height.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.__width = 0
        self.__height = 0
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """
        Deletes an instance of the rectangle.
        Prints a message indicating the deletion of the instance,
        and decrements the number of instances counter.
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

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

    def __str__(self):
        """
        Returns a string representation of the rectangle,
        with the given print_symbol forming the shape of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        picture = "\n".join([str(self.print_symbol) * self.__width
                             for _ in range(self.__height)])
        return picture

    def __repr__(self):
        """
        Returns a string representation of the rectangle,
        which can be used to recreate a new instance of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles and returns the one with the larger area.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.
        Returns:
            Rectangle: The rectangle with the larger area.
                If the areas are equal, returns rect_1.
        Raises:
            TypeError: If either rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
