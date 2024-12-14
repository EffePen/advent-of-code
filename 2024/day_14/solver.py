
import re
import math
import operator
from functools import reduce
from collections import Counter
import matplotlib.pyplot as plt


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    pattern = re.compile(r"p=(.+),(.+) v=(.+),(.+)")
    robots = [(int(px) + int(py)*1j, int(vx) + int(vy)*1j) for px, py, vx, vy in re.findall(pattern, input_txt)]
    return robots


def complex_mod(x, y):
    return (x.real % y.real) + (x.imag % y.imag) * 1j


def quadrant(p, middle_point):
    qx, qy = 0, 0
    if p.real < middle_point.real:
        qx = -1
    elif p.real > middle_point.real:
        qx = +1

    if p.imag < middle_point.imag:
        qy = -1
    elif p.imag > middle_point.imag:
        qy = +1
    return qx, qy


def solve_pt1(robots, grid_shape, num_seconds):
    grid_w, grid_h = grid_shape
    middle_point = int(math.floor(grid_w / 2)) + int(math.floor(grid_h / 2)) * 1j
    final_positions = [complex_mod(p + v * num_seconds, grid_shape[0] + grid_shape[1] * 1j) for p, v in robots]
    quadrants = [quadrant(p, middle_point) for p in final_positions]
    score = reduce(operator.mul, Counter([q for q in quadrants if 0 not in q]).values(), 1)
    return score


def solve_pt2(robots, grid_shape):
    idx = 0

    while True:
        robots = [(complex_mod(p + v, (grid_shape[0] + grid_shape[1] * 1j)), v) for p, v in robots]
        idx += 1
        ps = set([p for p, v in robots])
        xs_counter = Counter([p.real for p in ps])
        ys_counter = Counter([p.imag for p in ps])

        # print image if there is a concentration of points in a single row or column
        if (any([v > 20 for v in xs_counter.values()])
                or any([v > 20 for v in ys_counter.values()])):
            fig, ax = plt.subplots()
            ax.scatter(x=[p.real for p in ps], y=[grid_shape[1] - p.imag for p in ps])
            plt.savefig(f"images/{idx}.png")


# PARSE INPUT
robots = parse_input()

# PART 1
score = solve_pt1(robots, grid_shape=(101, 103), num_seconds=100)
print(f"Part 1 solution: {score}")


# PART 2
# NOTE: to solve this, you need to manually inspect
solve_pt2(robots, grid_shape=(101, 103))
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass