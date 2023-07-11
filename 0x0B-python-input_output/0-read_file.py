#!/usr/bin/python3
"""
Module 0-read_file
Contains a function that reads and prints the contents from a file.
"""


def read_file(filename=""):
    """
    Read and print the text from a file.
    Parameters:
        - filename (str): The name of the file to read.

    Returns:
        - None
    Raises:
        - FileNotFoundError: If the file does not exist.
        - IOError: If there is an error reading the file.
    """
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            print(file.read(), end="")
    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: Unable to read the file.")
