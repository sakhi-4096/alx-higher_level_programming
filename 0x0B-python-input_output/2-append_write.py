#!/usr/bin/python3
"""
Module 4-append_write
Contains a function that appends text to a file and returns the
number of characters added.
"""


def append_write(filename="", text=""):
    """
    Append text to a file and return the number of characters added.
    Parameters:
        - filename (str): The name of the file to append.
        - text (str): The text to append to the file.
    Returns:
        - int: The number of characters added.
    Raises:
        - IOError: If there is an error appending to the file.
    """
    try:
        with open(filename, mode="a", encoding="utf-8") as file:
            return file.write(text)
    except IOError:
        print("Error: Unable to append to the file.")
        return 0
