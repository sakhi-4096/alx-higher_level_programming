#!/usr/bin/python3
"""
Module 100-append_after

Contains function that appends str after lines that include keyword
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Appends new_string after lines that include search_string in the file.
    """
    with open(filename, mode="r+", encoding="utf-8") as file:
        lines = file.readlines()
        modified_lines = []
        for line in lines:
            modified_lines.append(line)
            if search_string in line:
                modified_lines.append(new_string)
        file.seek(0)
        file.truncate()
        file.writelines(modified_lines)
