#!/usr/bin/python3
"""
Module 12-pascal_triangle

Contains function that returns int lists of pascal triangle of any given size
"""

def pascal_triangle(n):
    """
    Return a list of integer lists representing Pascal's triangle of size n.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for _ in range(1, n):
        row = [1]
        prev_row = triangle[-1]
        for j in range(1, len(prev_row)):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
