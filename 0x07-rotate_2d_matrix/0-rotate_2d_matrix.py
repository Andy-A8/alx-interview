#!/usr/bin/python3
"""
     Given an n x n 2D matrix, rotate it 90 degrees clockwise.

    Prototype: def rotate_2d_matrix(matrix):
    Do not return anything. The matrix must be edited in-place.
    You can assume the matrix will have 2 dimensions and will not be empty.
    """


def transpose_matrix(matrix, n):
    """ Transpose the matrix """
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_matrix(matrix):
    """ Reverse each row """
    for row in matrix:
        row.reverse()


def rotate_2d_matrix(matrix):
    """ Function to rotate 2d matrix """
    n = len(matrix)

    transpose_matrix(matrix, n)

    reverse_matrix(matrix)

    return matrix
