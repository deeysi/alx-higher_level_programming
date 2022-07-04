#!/usr/bin/python3
"""
    1-my_list Module
"""


class MyList(list):
    """
        Mylist class
    """

    def print_sorted(self):
        """
            Prints a sorted list in ascending order
        """
        print(sorted(self))
