#!/usr/bin/python3
"""
Rotate 2D Matrix module
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of list of int): The matrix to rotate.

    Returns:
        None
    """
    n = len(matrix)
    # Transpose matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
