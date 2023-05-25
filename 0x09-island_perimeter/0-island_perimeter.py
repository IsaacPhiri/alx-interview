#!/usr/bin/python3
"""
Island perimeter module
"""


def island_perimeter(grid):
    """Calculates the perimeter aorund land=1
    """
    perimeter = 0
    # Iterate over each row in the grid
    for i in range(len(grid)):
        # Iterate over each element in the row
        for j in range(len(grid[i])):
            # Check if the current element represents land
            if grid[i][j] == 1:
                perimeter += 4  # Increment perimeter by 4 for a land cell
                # Check the adjacent cells (up, down, left, right)
                # and decrement perimeter for each shared side
                if i > 0 and grid[i-1][j] == 1:  # Check up
                    perimeter -= 1
                if i < len(grid) - 1 and grid[i+1][j] == 1:  # Check down
                    perimeter -= 1
                if j > 0 and grid[i][j-1] == 1:  # Check left
                    perimeter -= 1
                if j < len(grid[i]) - 1 and grid[i][j+1] == 1:  # Check right
                    perimeter -= 1

    return perimeter
