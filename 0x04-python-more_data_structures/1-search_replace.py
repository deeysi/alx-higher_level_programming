#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element by another in a new list.

    Args:
        my_list: list to replace from
        search: the element to replace in the list
        replace: the new element

    Return:
        new list containing the replaced elements
    """
    return [num if (num != search) else replace for num in my_list]
