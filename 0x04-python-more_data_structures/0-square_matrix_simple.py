#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix

    Args:
        matrix: 2D list to perform operation on

    Return:
        same size and square of all value of a matrix
    """
    new_list = []
    for item in matrix:
        new_list.append(list(map(lambda x: x ** 2, item)))
    return new_list
