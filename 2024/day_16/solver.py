
import math
from collections import defaultdict


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    grid = {c_idx + 1j*r_idx: c for r_idx, row in enumerate(input_txt.splitlines())
                                for c_idx, c in enumerate(row) if c != "#"}
    return grid


def solve_pt1(grid):
    visited = dict()
    start, = [p for p in grid if grid[p] == "S"]
    end, = [p for p in grid if grid[p] == "E"]
    dir = +1
    curr_statuses = {(start, dir, 0)}
    end_values = list()

    while curr_statuses:
        p, d, v = curr_statuses.pop()
        if visited.get((p, d), math.inf) < v or p not in grid:
            continue
        if p == end:
            end_values.append(v)
        visited[(p, d)] = v
        curr_statuses.update([(p+d, d, v+1), (p+d*1j, d*1j, v+1001), (p+d*-1j, d*-1j, v+1001), (p-d, -d, v+2001)])
    score = min(end_values)
    return score


def solve_pt2(grid, best_val):
    score = 0
    return score


# PARSE INPUT
grid = parse_input()

# PART 1
score = solve_pt1(grid)
print(f"Part 1 solution: {score}")


# PART 2
score = solve_pt2(grid)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass