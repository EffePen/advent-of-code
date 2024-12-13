

import re
import numpy as np


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    pattern = re.compile(r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)")
    machine_configs = [[int(e) for e in mc] for mc in re.findall(pattern, input_txt)]
    return machine_configs


def solve(machine_configs, delta=0):
    cost = 0
    for ax, ay, bx, by, px, py in machine_configs:
        # solve linear equations via matrix inversion and multiplication
        sol = np.matmul(np.linalg.inv(np.array([[ax, bx], [ay, by]], dtype=np.int64)), np.array([px + delta, py + delta], dtype=np.int64))
        if all([round(e, 3).is_integer() for e in sol]): # only integer solutions (round due to float operations errors)
            cost += sol[0] * 3 + sol[1] * 1
    return cost


# PARSE INPUT
machine_configs = parse_input()

# PART 1
score = solve(machine_configs, delta=0)
print(f"Part 1 solution: {score}")

# PART 2
score = solve(machine_configs, delta=10000000000000)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass
