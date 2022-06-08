#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    returns the weighted average of all integers tuple (<score>, <weight>)

    Args:
        my_list: initial list

    Return:
        average of all integer tuples
    """
    if not my_list:
        return 0
    denominator = 0
    new_list = []
    for first, second in my_list:
        new_list.append(first * second)
        denominator += second
    return sum(new_list) / denominator
