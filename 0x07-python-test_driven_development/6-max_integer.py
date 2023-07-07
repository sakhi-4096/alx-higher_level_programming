#!/usr/bin/python3


def max_integer(lst=None):
    """Find and return the maximum integer in a list.

    Args:
        lst (list): The list of integers.
    Returns:
        int: The maximum integer in the list.
        None: If the list is empty.
    Raises:
        TypeError: If lst is not a list.
    """
    if lst is None:
        lst = []
    if not isinstance(lst, list):
        raise TypeError("lst must be a list")

    if len(lst) == 0:
        return None

    result = lst[0]
    for num in lst[1:]:
        if num > result:
            result = num

    return result
