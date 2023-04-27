#!/usr/bin/python3
"""SolutionFinder module for N Queens problem"""


import sys


BOARD_SIZE = 0
"""The size of the chessboard."""

POSSIBLE_SOLUTIONS = []
"""The list of possible solutions to the N queens problem."""

POSSIBLE_POSITIONS = None
"""The list of possible positions on the chessboard."""


def retrieve_input():
    """Retrieves and validates the program argument.
    Returns:
        int: The size of the chessboard.
    """
    global BOARD_SIZE
    BOARD_SIZE = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        BOARD_SIZE = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if BOARD_SIZE < 4:
        print("N must be at least 4")
        sys.exit(1)
    return BOARD_SIZE


def is_attacking(pos0, pos1):
    """Checks if the positions of two queens are in an attacking mode.
    Args:
        pos0 (list or tuple): The first queen's position.
        pos1 (list or tuple): The second queen's position.
    Returns:
        bool: True if the queens are in an attacking position else False.
    """
    if (pos0[0] == pos1[0]) or (pos0[1] == pos1[1]):
        return True
    return abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])


def does_group_exist(group):
    """Checks if a group exists in the list of solutions.
    Args:
        group (list of integers): A group of possible positions.
    Returns:
        bool: True if it exists, otherwise False.
    """
    global POSSIBLE_SOLUTIONS
    for stn in POSSIBLE_SOLUTIONS:
        i = 0
        for stn_pos in stn:
            for grp_pos in group:
                if stn_pos[0] == grp_pos[0] and stn_pos[1] == grp_pos[1]:
                    i += 1
        if i == BOARD_SIZE:
            return True
    return False


def build_solution(row, group):
    """Builds a solution for the n queens problem.
    Args:
        row (int): The current row in the chessboard.
        group (list of lists of integers): The group of valid positions.
    """
    global POSSIBLE_SOLUTIONS
    global BOARD_SIZE
    if row == BOARD_SIZE:
        tmp0 = group.copy()
        if not does_group_exist(tmp0):
            POSSIBLE_SOLUTIONS.append(tmp0)
    else:
        for col in range(BOARD_SIZE):
            a = (row * BOARD_SIZE) + col
            matches = zip(list([POSSIBLE_POSITIONS[a]]) * len(group), group)
            used_positions = map(lambda x: is_attacking(x[0], x[1]), matches)
            group.append(POSSIBLE_POSITIONS[a].copy())
            if not any(used_positions):
                build_solution(row + 1, group)
            group.pop(len(group) - 1)


def get_solutions():
    """Gets the solutions for the given chessboard size.
    """
    global POSSIBLE_POSITIONS, BOARD_SIZE
    POSSIBLE_POSITIONS = list(
                            map(lambda x: [x // BOARD_SIZE, x % BOARD_SIZE],
                                range(BOARD_SIZE ** 2))
                            )
    a = 0
    group = []
    build_solution(a, group)


n = retrieve_input()
get_solutions()
for solution in POSSIBLE_SOLUTIONS:
    print(solution)
