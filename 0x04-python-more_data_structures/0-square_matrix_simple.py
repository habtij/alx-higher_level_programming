#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix"""
    new_matrix = []
    if len(matrix) != 0:
        for i in range(len(matrix)):
            new_matrix.append(list(map(lambda x: x**2, matrix[i])))

    return(new_matrix)
