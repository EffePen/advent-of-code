

import re
from collections import defaultdict


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()

    codes = input_txt.splitlines()

    # numpad grid
    pad = defaultdict(dict)
    pad["numpad"].update({c_idx + 0j: num for c_idx, num in enumerate(["7", "8", "9"])})
    pad["numpad"].update({c_idx + 1j: num for c_idx, num in enumerate(["4", "5", "6"])})
    pad["numpad"].update({c_idx + 2j: num for c_idx, num in enumerate(["1", "2", "3"])})
    pad["numpad"].update({c_idx + 3j: num for c_idx, num in enumerate(["0", "A"], start=1)})

    # dirpad grid
    pad["dirpad"].update({c_idx + 0j: num for c_idx, num in enumerate(["^", "A"], start=1)})
    pad["dirpad"].update({c_idx + 1j: num for c_idx, num in enumerate(["<", "v", ">"])})

    return codes, pad


def solve_pt1(codes, pad):
    dir_map = {"^": -1j, "<": -1, "v": 1j, ">": 1}

    rev_pad = {pad_type: {v:k for k, v in pad_dict.items()} for pad_type, pad_dict in pad.items()}

    distances = {}
    for pad_type in pad:
        distances[pad_type] = {(k1, k2): k2_pos - k1_pos
                               for k1_pos, k1 in pad[pad_type].items()
                               for k2_pos, k2 in pad[pad_type].items()}

    score = 0
    for code in codes:
        numeric_part = int("".join(re.findall(r"\d", code)))
        for pad_type in ["numpad"] + ["dirpad"] * 2:
            prev_c = "A"
            new_code = ""
            for curr_c in code:
                dist = distances[pad_type][(prev_c, curr_c)]
                # check if intermediate position is valid
                if rev_pad[pad_type][curr_c] + dist.real in pad[pad_type]:
                    new_code += int(abs(dist.real)) * ("<" if dist.real < 0 else ">") + int(abs(dist.imag)) * ("^" if dist.imag < 0 else "v") + "A"
                else:
                    new_code += int(abs(dist.imag)) * ("^" if dist.imag < 0 else "v") + int(abs(dist.real)) * ("<" if dist.real < 0 else ">") + "A"
                prev_c = curr_c
            code = new_code
        code_len = len(code)
        score += code_len * numeric_part

    return score


def solve_pt2(codes, pad):
    score = 0
    return score



# PARSE INPUT
codes, pad = parse_input()

# PART 1
score = solve_pt1(codes, pad)
print(f"Part 1 solution: {score}")


# PART 2
score = solve_pt2(codes, pad)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass