#!/usr/bin/python3


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number and
    returns a new matrix.

    Args:
        matrix (list): The matrix represented as a list of lists
                       of integers or floats.
        div (int or float): The divisor.
    Returns:
        list: A new matrix with the divided elements.
    Raises:
        TypeError: If div is not an instance of int or float.
        ZeroDivisionError: If div is zero.
        TypeError: If matrix is not a valid matrix.
        TypeError: If any element in the matrix is not an instance
                   of int or float.
        TypeError: If any row in the matrix has a different size.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or len(matrix) == 0 or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    new_matrix = []
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_row.append(round(element / div, 2))

        new_matrix.append(new_row)

    return new_matrix
