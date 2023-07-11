#!/usr/bin/python3
"""
Module 1-my_list
Contains class MyList
Inherits from list;  public instance method to print sorted
"""


class MyList(list):
    """ Inherits from list
    Methods:
    print_sorted()
    """
    def print_sorted(self):
        """ Print list of ints all sorted in ascending order """
        print(sorted(self))
