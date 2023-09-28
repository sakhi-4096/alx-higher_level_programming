#!/usr/bin/python3
"""Finds a peak element in a list of unsorted integers."""


def find_peak(list_of_integers):
    """
    Finds a peak element in a list of unsorted integers.
    """
    # check if the input list is empty
    if not list_of_integers:
        return None

    # initialize the search range
    left = 0
    right = len(list_of_integers) - 1

    # perform binary search to find a peak
    while left < right:
        mid = (left + right) // 2

        # compare the middle element with its right neighbor
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    # the peak element is found at 'left' index
    return list_of_integers[left]
