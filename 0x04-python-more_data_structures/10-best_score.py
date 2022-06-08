#!/usr/bin/python3
def best_score(a_dictionary):
    """
    returns a key with the biggest integer value

    Args:
        a_dictionary: intial dictionary

    Return:
        key with biggest integer value or none
        if score is not found
    """
    if not a_dictionary:
        return None
    return max(a_dictionary, key=lambda x: a_dictionary[x])
