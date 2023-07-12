#!/usr/bin/python3
"""
Module 3-to_json_string
Contains a function that returns the JSON representation of a Python object
as a string.
"""


def to_json_string(my_obj):
    """
    Return the JSON representation of a Python object as a string.
    Parameters:
        - my_obj: The Python object to convert to JSON.
    Returns:
        - str: The JSON representation of the object as a string.
    """
    import json

    return json.dumps(my_obj)
