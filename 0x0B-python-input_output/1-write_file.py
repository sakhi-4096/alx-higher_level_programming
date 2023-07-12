#!/usr/bin/python3
"""
Module 3-write_file
Contains a function that writes text to a file and returns the
number of characters written.
"""


def write_file(filename="", text=""):
    """
    Write text to a file and return the number of characters written.
    Parameters:
        - filename (str): The name of the file to write.
        - text (str): The text to write to the file.

    Returns:
        - int: The number of characters written.

    Raises:
        - IOError: If there is an error writing to the file.

    """
    try:
        with open(filename, mode="w", encoding="utf-8") as file:
            return file.write(text)
    except IOError:
        print("Error: Unable to write to the file.")
        return 0
