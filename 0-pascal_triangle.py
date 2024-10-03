#!/usr/bin/python3
"""
    A script to represent the pascal's triangle for any given number
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n
    or an empty list if n <= 0.
    """
    triangle = []

    if n <= 0:
        return triangle
    for i in range(n):
        temp_list = []

        for j in range(i+1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(temp_list)

    return triangle
