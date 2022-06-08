#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    replaces or adds key/value in a dictionary

    Args:
        a_dictionary: initial dictiornary
        key: key to be updated
        value: value to be updated

    Return:
        updated dictionary
    """
    a_dictionary.update({key: value})
    return a_dictionary
