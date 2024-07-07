

import re
import numpy as np
from collections import Counter


def parse_input():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    specs = {}
    for l in lines:
        (cid, x, y, w, h), = [[int(e) for e in m] for m in
                           re.findall("#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)", l)]
        specs[cid] = (x, y, w, h)

    return specs


def solve_pt1(specs):
    full_square = np.zeros(shape=(1000, 1000))
    for (x, y, w, h) in specs.values():
        full_square[x:x+w, y:y+h] += 1
    score = (full_square >= 2).sum()
    return score


def solve_pt2(specs):
    for s1_idx, (x1, y1, w1, h1) in specs.items():
        x11, x12 = x1 + 1, x1 + w1
        y11, y12 = y1 + 1, y1 + h1

        overlaps = False
        for s2_idx, (x2, y2, w2, h2) in specs.items():
            if s1_idx != s2_idx:
                x21, x22 = x2 + 1, x2 + w2
                y21, y22 = y2 + 1, y2 + h2

                if not (
                    max([x21, x22]) < min([x11, x12]) or
                    max([x11, x12]) < min([x21, x22]) or
                    max([y21, y22]) < min([y11, y12]) or
                    max([y11, y12]) < min([y21, y22])
                ):
                    overlaps = True
                    break
        if not overlaps:
            return s1_idx


specs = parse_input()


# ######## PART 1
score = solve_pt1(specs)
print("Part 1 solution: ", score)


# ######## PART 2
pt2_sol = solve_pt2(specs)
print("Part 2 solution: ", pt2_sol)


if __name__ == "__main__":
    pass