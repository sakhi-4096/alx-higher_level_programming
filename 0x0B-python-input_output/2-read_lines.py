#!/usr/bin/python3
"""
Module 2-read_lines
Contains a function that reads and prints a specified number of lines from a
text file.
"""


def read_lines(filename="", nb_lines=0):
    """
    Read and print a specified number of lines from a text file.
    Parameters:
        - filename (str): The name of the file to read.
        - nb_lines (int): The number of lines to read and print. If nb_lines
                  is less than or equal to 0, the entire file will be printed.
    Returns:
        None
    Raises:
        - FileNotFoundError: If the file does not exist.
        - IOError: If there is an error reading the file.
    """
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            if nb_lines <= 0:
                print(file.read(), end="")
            else:
                for _ in range(nb_lines):
                    line = file.readline()
                    if not line:
                        break
                    print(line, end="")
    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: Unable to read the file.")
