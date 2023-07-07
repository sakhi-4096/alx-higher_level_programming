#!/usr/bin/python3


def matrix_mul(m_a, m_b):
    """
    Perform matrix multiplication and return the resulting matrix.

    Args:
        m_a (list): Matrix A represented as a list of lists
        containing ints or floats.
        m_b (list): Matrix B represented as a list of lists
        containing ints or floats.
    Returns:
        list: Resulting matrix after performing matrix multiplication.
    Raises:
        TypeError: If either m_a or m_b is not a list.
        ValueError: If either m_a or m_b is empty or contains [[]].
        TypeError: If m_a or m_b contains elements other than ints or floats.
        TypeError: If the rows of m_a are not of the same size.
        ValueError: If the number of columns in m_a is not equal to the
        number of rows in m_b.
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a and m_b must be lists.")

    if len(m_a) == 0 or len(m_b) == 0 or m_a == [[]] or m_b == [[]]:
        raise ValueError("m_a and m_b cannot be empty.")

    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats.")
        if len(row) != len(m_a[0]):
            raise TypeError("Each row of m_a must have the same size.")
        if len(row) != len(m_b):
            raise ValueError("m_a and m_b cannot be multiplied.")

    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats.")
        if len(row) != len(m_b[0]):
            raise TypeError("Each row of m_b must have the same size.")

    new_matrix = []
    for row_a in range(len(m_a)):
        new_row = []
        for col_b in range(len(m_b[0])):
            element_sum = 0
            for i in range(len(m_a[0])):
                element_sum += m_a[row_a][i] * m_b[i][col_b]
            new_row.append(element_sum)
        new_matrix.append(new_row)

    return new_matrix
