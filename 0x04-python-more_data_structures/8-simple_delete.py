#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    deletes a key in a dictionary.

    Args:
        a_dictionary: initial dictionary
        key: key to be deleted

    Return:
        updated dictionary
    """
    if a_dictionary.get(key):
        a_dictionary.pop(key)
    return a_dictionary
