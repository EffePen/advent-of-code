
import numpy as np


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    ranges_txt, ingredients_txt = input_txt.split("\n\n")
    ranges = [(int(e.split("-")[0]), int(e.split("-")[1])) for e in ranges_txt.splitlines()]
    ingredients = [int(e) for e in ingredients_txt.splitlines()]
    return ranges, ingredients


def solve_pt1(ranges, ingredients):
    score = 0
    sorted_ranges = sorted(ranges)
    sorted_ingredients = sorted(ingredients)

    min_r_idx = 0
    for ingredient in sorted_ingredients:
        ok_range_idxs = []
        for d_r_idx, (r_min, r_max) in enumerate(sorted_ranges[min_r_idx:]):
            if r_min <= ingredient <= r_max:
                ok_range_idxs.append(min_r_idx + d_r_idx)
            elif ok_range_idxs:
                break

        if ok_range_idxs:
            min_r_idx = min(ok_range_idxs)
            score += 1
    return score


def solve_pt2(ranges):
    score = 0
    sorted_ranges = sorted(ranges)
    new_ranges = [sorted_ranges[0]]

    for r_min, r_max in sorted_ranges[1:]:
        last_r_min, last_r_max = new_ranges[-1]
        if last_r_min <= r_min <= last_r_max:
            new_ranges[-1] = (last_r_min, max(r_max, last_r_max))
        else:
            new_ranges.append((r_min, r_max))

    for new_r_min, new_r_max in new_ranges:
        score += new_r_max - new_r_min + 1

    return score


# PARSE INPUT
ranges, ingredients = parse_input()

# PART 1
score = solve_pt1(ranges, ingredients)
print(f"Part 1 solution: {score}")


# PART 2
score = solve_pt2(ranges)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass