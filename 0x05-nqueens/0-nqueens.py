#!/usr/bin/python3
"""N queens"""

import sys


def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]"""

    # Check this row on left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True


def solve(board, col, n):
    """Recursive function to solve the N queens problem"""

    # Base case: If all queens are placed, return True
    if col >= n:
        print(board)
        return True

    # Consider this column and try placing a queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place the queen at board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            solve(board, col + 1, n)

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove the queen from board[i][col]
            board[i][col] = 0

    # If the queen can't be placed in any row in this column, then return False
    return False


if __name__ == '__main__':
    # Parse command line argument
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize an empty board
    board = [[0 for x in range(n)] for y in range(n)]

    solve(board, 0, n)
