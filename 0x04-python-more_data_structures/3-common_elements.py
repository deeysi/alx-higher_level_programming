#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    returns a set of common elements in two sets.

    Args:
        set_1: first set
        set_2: second set to be compared

    Return:
        a set of common elements in two sets
    """
    return set_1.intersection(set_2)
