

import re
import numpy as np


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    pattern = re.compile(r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)")
    machine_configs = [[int(e) for e in mc] for mc in re.findall(pattern, input_txt)]
    return machine_configs


def solve(machine_configs, part):
    cost = 0
    delta = 0 if part == 1 else 10000000000000
    for ax, ay, bx, by, px, py in machine_configs:
        # solve linear equations via matrix inversion and multiplication
        M = np.array([[ax, bx], [ay, by]], dtype=np.int64)

        # intersecting lines: get the unique integer solution
        if np.linalg.det(M) != 0:
            sol = np.matmul(np.linalg.inv(M), np.array([px + delta, py + delta], dtype=np.int64))
            if not all(round(e, 3).is_integer() for e in sol):
                continue
        # overlapping lines: get the lowest cost solution, if any
        elif ax / ay == bx / by == px / py:
            na, nb = px / ax, px / bx
            if round(na, 3).is_integer() and round(nb, 3).is_integer():
                sol = [na, 0.] if na * 3 < nb else [0., nb]
            elif round(na, 3).is_integer():
                sol = [na, 0.]
            elif round(nb, 3).is_integer():
                sol = [0., nb]
            else:
                continue
        # parallel lines: skip
        else:
            continue

        # check additional problem conditions
        if all((part == 2 or e < 100) for e in sol):
            cost += sol[0] * 3 + sol[1] * 1
    return cost


# PARSE INPUT
machine_configs = parse_input()

# PART 1
score = solve(machine_configs, part=1)
print(f"Part 1 solution: {score}")

# PART 2
score = solve(machine_configs, part=2)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass
