#!/usr/bin/python3
"""
Module 8-load_from_json_file
Contains a function that creates a Python object from a JSON file.
"""


def load_from_json_file(filename):
    """
    Create a Python object from a JSON file.
    Parameters:
        - filename: The JSON file to load the object from.
    Returns:
        - The Python object created from the JSON file.
    """
    import json

    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
