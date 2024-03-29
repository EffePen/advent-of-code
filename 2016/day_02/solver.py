

import math


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    steps = [list(e) for e in input_txt.splitlines()]
    return steps


# PARSE INPUT
steps = parse_input()
dir_map = {"D": (1, 0), "U": (-1, 0), "L": (0, -1), "R": (0, 1)}


# PART 1
def solve_part_1():
    MIN_P0 = MIN_P1 = 0
    MAX_P0 = MAX_P1 = 2

    pos2number_map = {((n-1) // 3, (n-1) % 3): str(n) for n in range(1, 10)}
    number2pos_map = {n: p for p, n in pos2number_map.items()}

    code_list = ["5"]

    for step in steps:
        p0, p1 = number2pos_map[code_list[-1]]
        for dir in step:
            d0, d1 = dir_map[dir]
            p0 = max(min(p0 + d0, MAX_P0), MIN_P0)
            p1 = max(min(p1 + d1, MAX_P1), MIN_P1)
        new_num = pos2number_map[(p0, p1)]
        code_list.append(new_num)

    print(f"Part 1 solution: {''.join([str(e) for e in code_list[1:]])}")

solve_part_1()


# PART 2
def solve_part_2():

    keypad_layout = """
      1
     234
    56789
     ABC
      D
    """

    pos2number_map = dict()
    for l_idx, l in enumerate(keypad_layout.splitlines()):
        for c_idx, c in enumerate(l):
            pos2number_map[(l_idx, c_idx)] = c
    number2pos_map = {n: p for p, n in pos2number_map.items()}

    code_list = ["5"]

    for step in steps:
        p0, p1 = number2pos_map[code_list[-1]]
        for dir in step:
            d0, d1 = dir_map[dir]
            c = pos2number_map.get((p0 + d0, p1 + d1))
            if not (c is None or c.strip() == ""):
                p0, p1 = (p0 + d0, p1 + d1)
        new_num = pos2number_map[(p0, p1)]
        code_list.append(new_num)

    print(f"Part 1 solution: {''.join([str(e) for e in code_list[1:]])}")


solve_part_2()


if __name__ == "__main__":
    pass