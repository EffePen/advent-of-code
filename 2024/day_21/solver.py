

import re
from functools import cache
from collections import defaultdict, Counter


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
    # consider only straight paths (horizontal first, then vertical and vice-versa)
    # since the mixed horizontal-vertical sequences would lead to longer sequences
    base_transform = {}
    for pad_type in key2pos:
        base_transform[pad_type] = {}
        for k1, k1_pos in key2pos[pad_type].items():
            for k2, k2_pos in key2pos[pad_type].items():
                dist = k2_pos - k1_pos
                tmp_codes = set()
                if key2pos[pad_type][k1] + dist.real in key2pos[pad_type].values():
                    tmp_codes.add(int(abs(dist.real)) * ("<" if dist.real < 0 else ">") + int(abs(dist.imag)) * ("^" if dist.imag < 0 else "v") + "A")
                if key2pos[pad_type][k1] + 1j * dist.imag in key2pos[pad_type].values():
                    tmp_codes.add(int(abs(dist.imag)) * ("^" if dist.imag < 0 else "v") + int(abs(dist.real)) * ("<" if dist.real < 0 else ">") + "A")
                base_transform[pad_type][k1+k2] = tmp_codes
    return codes, base_transform


def get_recurse_fn(base_transform):
    @cache
    def recurse(codes_counter, pads):
        score = 0
        curr_pad, next_pads = pads[0], pads[1:]

        # NOTE: since each sub-code ends with "A" => each sub-code is preceded by "A" => they can evolve independently
        for code, cnt in codes_counter:
            # prepare all alternative new code lists: fork when multiple base transformations for the same char pairs
            new_code_lists = [[]]
            for idx in range(len(code)):
                tmp_new_codes = []
                for par_path in base_transform[curr_pad][("A" + code)[idx:idx+2]]:
                    tmp_new_codes += [nc + [par_path] for nc in new_code_lists]
                new_code_lists = tmp_new_codes

            # calculate new counters and increase count "cnt" times
            new_codes_counters = [Counter(ncl) for ncl in new_code_lists]
            new_codes_counters = [{new_code: new_cnt * cnt for new_code, new_cnt in c.items()} for c in new_codes_counters]

            # keep only the shortest sequence
            if len(pads) == 1:
                score += min(sum(len(new_code) * new_cnt for new_code, new_cnt in cc.items()) for cc in new_codes_counters)
            else:
                score += min(recurse(tuple(cc.items()), pads=next_pads) for cc in new_codes_counters)
        return score

    return recurse


def solve(codes, base_transform, num_iter):
    # prepare recurse function
    recurse_fn = get_recurse_fn(base_transform)

    score = 0
    for code in codes:
        # extract numeric part from initial code
        numeric_part = int("".join(re.findall(r"\d", code)))

        # iterate over pads recursively and get total length
        code_len = recurse_fn(((code, 1),), pads=tuple(["numpad"] + num_iter * ["dirpad"]))
        score += numeric_part * code_len

    return score


# PARSE INPUT
codes, base_transform = parse_input()


# PART 1
score = solve(codes, base_transform, num_iter=2)
print(f"Part 1 solution: {score}")


# PART 2
score = solve(codes, base_transform, num_iter=25)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass