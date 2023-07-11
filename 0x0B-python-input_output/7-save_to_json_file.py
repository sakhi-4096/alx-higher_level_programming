#!/usr/bin/python3
"""
Module 7-save_to_json_file
Contains a function that writes a Python object to a file using
JSON representation.
"""


def save_to_json_file(my_obj, filename):
    """
    Write a Python object to a file using JSON representation.
    Parameters:
        - my_obj: The Python object to be written.
        - filename: The file to write the object to.
    """
    import json

    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
