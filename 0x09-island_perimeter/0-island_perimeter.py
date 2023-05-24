#!/usr/bin/python3

def island_perimeter(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Each land cell contributes 4 to the perimeter

                # Check left neighbor
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Deduct 2 if left neighbor is also land

                # Check top neighbor
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Deduct 2 if top neighbor is also land

    return perimeter
