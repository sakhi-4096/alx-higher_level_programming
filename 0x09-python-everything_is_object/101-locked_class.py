#!/usr/bin/python3
"""
Defines a class that restricts the creation of new instance
attributes dynamically.
Only the attribute "first_name" is allowed.
"""


class LockedClass:
    """
    Class that prevents the creation of new instance attributes dynamically,
    except for the attribute "first_name".
    """

    __slots__ = ("first_name",)
