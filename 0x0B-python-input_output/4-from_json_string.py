#!/usr/bin/python3
"""
Module 4-from_json_string
Contains a function that returns a Python data structure
from a JSON string.
"""


def from_json_string(my_str):
    """
    Return a Python data structure from a JSON string.
    Parameters:
        - my_str: The JSON string representation.
    Returns:
        - object: The Python data structure.
    """
    import json

    return json.loads(my_str)
