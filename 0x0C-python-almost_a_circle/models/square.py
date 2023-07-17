#!/usr/bin/python3
"""Square class inherited from Rectangle."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inherited from Rectangle.

    Attributes:
        size (int): Size of the square side.
        x (int): X-coordinate of the square.
        y (int): Y-coordinate of the square.
        id (int): ID of the square instance.

    Methods:
        __init__(self, size, x=0, y=0, id=None): Initialize a Square instance.
        __str__(self): Get a string representation of the Square.
        update(self, *args, **kwargs): Update attributes of the Square.
        to_dictionary(self): Get the dictionary representation of the Square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
            size (int): Size of the square side.
            x (int, optional): X-coordinate of the square. Default is 0.
            y (int, optional): Y-coordinate of the square. Default is 0.
            id (int, optional): ID of the square instance. If not provided,
                                it will be automatically assigned.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Get the size of the square side.

        Returns:
            int: Size of the square side.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square side.

        Args:
            value (int): Size of the square side.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Get a string representation of the Square.

        Returns:
            str: String representation of the Square.
        """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(self.__class__.__name__, self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """
        Update attributes of the Square.

        Args:
            *args: Variable length argument list containing new
                   attribute values.
            **kwargs: Arbitrary keyword arguments with attribute
                 names as keys and new attribute values as values.
        """
        attrs = ['id', 'size', 'x', 'y']
        if args:
            for i, arg in enumerate(args):
                if i >= len(attrs):
                    break
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Get the dictionary representation of the Square.

        Returns:
            dict: Dictionary representation of the Square attributes.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y,
        }
