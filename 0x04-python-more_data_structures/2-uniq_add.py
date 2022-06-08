#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    adds all unique integers in a list (only once for each integer)

    Args:
        my_list: initial list

    Return:
        addition of unique list elements
    """
    return sum(set(my_list))
