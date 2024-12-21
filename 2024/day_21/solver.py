

import re
from functools import cache
from collections import defaultdict


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()

    codes = input_txt.splitlines()

    # numpad grid
    key2pos = defaultdict(dict)
    key2pos["numpad"].update({num: c_idx + 0j for c_idx, num in enumerate(["7", "8", "9"])})
    key2pos["numpad"].update({num: c_idx + 1j for c_idx, num in enumerate(["4", "5", "6"])})
    key2pos["numpad"].update({num: c_idx + 2j for c_idx, num in enumerate(["1", "2", "3"])})
    key2pos["numpad"].update({num: c_idx + 3j for c_idx, num in enumerate(["0", "A"], start=1)})

    # dirpad grid
    key2pos["dirpad"].update({num: c_idx + 0j for c_idx, num in enumerate(["^", "A"], start=1)})
    key2pos["dirpad"].update({num: c_idx + 1j for c_idx, num in enumerate(["<", "v", ">"])})

    # pre-calculate transforms
    base_transform = {}
    for pad_type in key2pos:
        base_transform[pad_type] = {}
        for k1, k1_pos in key2pos[pad_type].items():
            for k2, k2_pos in key2pos[pad_type].items():
                dist = k2_pos - k1_pos
                # NOTE: there is a bug. k2 should be k1
                if key2pos[pad_type][k2] + dist.real in key2pos[pad_type].values():
                    code = int(abs(dist.real)) * ("<" if dist.real < 0 else ">") + int(abs(dist.imag)) * ("^" if dist.imag < 0 else "v") + "A"
                else:
                    code = int(abs(dist.imag)) * ("^" if dist.imag < 0 else "v") + int(abs(dist.real)) * ("<" if dist.real < 0 else ">") + "A"
                base_transform[pad_type][k1+k2] = code
    return codes, base_transform


def solve_pt1(codes, base_transform):
    score = 0
    for code in codes:
        numeric_part = int("".join(re.findall(r"\d", code)))
        # from numpad to dirpad
        new_codes = [base_transform["numpad"][prev_c + curr_c] for prev_c, curr_c in zip("A" + code[:-1], code)]

        # iterate over robot dirpads
        for idx in range(2):
            code = "".join(new_codes)
            new_codes = [base_transform["dirpad"][prev_c + curr_c] for prev_c, curr_c in zip("A" + code[:-1], code)]
            code = "".join(new_codes)

        code_len = len(code)
        score += code_len * numeric_part

    return score


def solve_pt2(codes, pad):
    score = 0
    return score



# PARSE INPUT
codes, base_transform = parse_input()

# PART 1
score = solve_pt1(codes, base_transform)
print(f"Part 1 solution: {score}")


# PART 2
score = solve_pt2(codes, base_transform)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass