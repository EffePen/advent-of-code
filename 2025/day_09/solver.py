
import os
import ast
import math


def parse_input():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")) as f:
        input_txt = f.read()
    coords = [ast.literal_eval(f"({l})") for l in input_txt.splitlines()]
    return coords


def solve_pt1(coords):
    areas = []
    for c1_idx, c1 in enumerate(coords[:-1]):
        for c2 in coords[c1_idx+1:]:
            areas.append((abs(c1[0] - c2[0]) + 1) * (abs(c1[1] - c2[1]) + 1))
    return max(areas)


def solve_pt2(coords):
    score = 0
    return score



# PARSE INPUT
coords = parse_input()

# PART 1
score = solve_pt1(coords)
print(f"Part 1 solution: {score}")

# PART 2
score = solve_pt2(coords)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass