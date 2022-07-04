#!/usr/bin/python3
"""
    0-lookup Module
"""


def lookup(obj):
    """
        gets the list of available attributes and methods
        of an object

        Args:
            obj: initial object

        Returns:
            list of available attributes and methods of an object
    """
    return dir(obj)
