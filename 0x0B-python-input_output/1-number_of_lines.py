#!/usr/bin/python3
"""
Module 1-number_of_lines
Contains a function that returns the number of lines in a text file.
"""


def number_of_lines(filename=""):
    """
    Return the number of lines in a text file.
    Parameters:
        - filename (str): The name of the file to count the lines.

    Returns:
        - int: The number of lines in the file.

    Raises:
        - FileNotFoundError: If the file does not exist.
        - IOError: If there is an error reading the file.
    """
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            lines = sum(1 for _ in file)
        return lines
    except FileNotFoundError:
        print("Error: File not found.")
        return 0
    except IOError:
        print("Error: Unable to read the file.")
        return 0
