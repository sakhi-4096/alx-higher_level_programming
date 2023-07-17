#!/usr/bin/python3
"""Rectangle class, inherits from Base class."""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class, inherits from Base class.

    Args:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int, optional): x-coordinate of the rectangle's position.
                           Defaults to 0.
        y (int, optional): y-coordinate of the rectangle's position.
                           Defaults to 0.
        id (int, optional): ID of the rectangle. Defaults to None.

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int): x-coordinate of the rectangle's position.
        y (int): y-coordinate of the rectangle's position.
        id (int): ID of the rectangle.
    Methods:
        area(): Calculate the area of the rectangle.
        display(): Print a visual representation of the rectangle using '#'.
        __str__(): Return a string representation of the rectangle.
        update(*args, **kwargs): Update the rectangle's attributes using
                                 positional or keyword arguments.
        to_dictionary(): Return a dictionary representation of the
                         rectangle's attributes.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): x-coordinate of the rectangle's position.
                               Defaults to 0.
            y (int, optional): y-coordinate of the rectangle's position.
                               Defaults to 0.
            id (int, optional): ID of the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.__width = 0
        self.__height = 0
        self.__x = 0
        self.__y = 0
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for the width of the rectangle."""
        return self.__width

    @property
    def height(self):
        """Getter method for the height of the rectangle."""
        return self.__height

    @property
    def x(self):
        """Getter method for the x-coordinate of the rectangle's position."""
        return self.__x

    @property
    def y(self):
        """Getter method for the y-coordinate of the rectangle's position."""
        return self.__y

    @width.setter
    def width(self, value):
        """
        Setter method for the width of the rectangle.

        Args:
            value (int): New width value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Setter method for the height of the rectangle.

        Args:
            value (int): New height value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """
        Setter method for the x-coordinate of the rectangle's position.

        Args:
            value (int): New x-coordinate value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """
        Setter method for the y-coordinate of the rectangle's position.

        Args:
            value (int): New y-coordinate value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Print a visual representation of the rectangle using '#'."""
        print("\n" * self.__y + "\n".join(" " * self.__x +
              "#" * self.__width for i in range(self.__height)))

    def __str__(self):
        """Return a string representation of the rectangle."""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.__class__.__name__, self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        Update the rectangle's attributes using positional or keyword
        arguments.

        Args:
            *args: Variable length argument list containing attributes in
            the order: id, width, height, x, y.
            **kwargs: Arbitrary keyword arguments to update the attributes.
        Raises:
            TypeError: If the value of any argument is not an integer.
            ValueError: If the value of any argument (except id) is
                        less than 0.
        """
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                if i >= len(attrs):
                    break
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Return a dictionary representation of the rectangle's attributes.

        Returns:
            dict: A dictionary containing the rectangle's attributes
                  (id, width, height, x, y).
        """
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y,
        }
