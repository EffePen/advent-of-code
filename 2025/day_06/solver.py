

import os
import re


def parse_input():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")) as f:
        input_txt = f.read()
    return input_txt


def solve_pt1(input_txt):
    score = 0
    
    # Actually parse the input in a p1 specific way
    grid = [e.split() for e in input_txt.splitlines()]
    operators = grid[-1]
    numbers = zip(*grid[:-1])

    # Solve
    for op, numbs in zip(operators, numbers):
        res = eval(op.join(numbs))
        score += res
    return score


def solve_pt2(input_txt):
    score = 0
    
    # Actually parse the input in a p2 specific way
    trans_grid = "\n".join(["".join(e) for e in zip(*input_txt.splitlines())][::-1])

    # Solve
    for problem in re.split(r"\n\s+\n", trans_grid):
        op = problem[-1]
        numbs = [e.strip() for e in problem[:-1].strip().splitlines()]
        res = eval(op.join(numbs))
        score += res    
    return score


# PARSE INPUT
input_txt = parse_input()

# PART 1
score = solve_pt1(input_txt)
print(f"Part 1 solution: {score}")

# PART 2
score = solve_pt2(input_txt)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass