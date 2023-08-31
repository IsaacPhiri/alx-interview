#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """ returns the perimeter of the island described in grid """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] is 1:
                if i is 0 or grid[i - 1][j] is 0:
                    perimeter += 1
                if i is len(grid) - 1 or grid[i + 1][j] is 0:
                    perimeter += 1
                if j is 0 or grid[i][j - 1] is 0:
                    perimeter += 1
                if j is len(grid[i]) - 1 or grid[i][j + 1] is 0:
                    perimeter += 1
    return perimeter
