#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    returns a set of all elements present in only one set

    Args:
        set_1: first set to compare
        set_2: second set to compare

    Return:
        a set of all elements present in only one set
    """
    return set_1.symmetric_difference(set_2)
