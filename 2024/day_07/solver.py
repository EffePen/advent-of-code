

import re


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()

    equations = []
    for l in input_txt.splitlines():
        tot_txt, nums_txt = l.split(": ")
        tot = int(tot_txt)
        nums = [int(e) for e in nums_txt.split()]
        equations.append((tot, nums))

    return equations


def recurse_pt1(tot, first_num, reversed_nums):
    for n_idx, n in enumerate(reversed_nums):
        # if divisible
        if tot % n == 0:
            mul_attempt = recurse_pt1(tot // n, first_num, reversed_nums[n_idx+1:])
            if mul_attempt:
                return mul_attempt

        # otherwise try subtracting
        sub_attempt = recurse_pt1(tot - n, first_num, reversed_nums[n_idx+1:])
        return sub_attempt

    return first_num == tot


def solve_pt1(equations):
    score = 0

    for tot, nums in equations:
        original_tot = tot
        first_num = nums[0]
        res = recurse_pt1(tot, first_num, reversed_nums=nums[:0:-1])
        if res:
            score += original_tot

    return score


def recurse_pt2(tot, first_num, reversed_nums):
    for n_idx, n in enumerate(reversed_nums):
        # if divisible
        if tot % n == 0:
            mul_attempt = recurse_pt2(tot // n, first_num, reversed_nums[n_idx+1:])
            if mul_attempt:
                return mul_attempt

        # if de-concatenation
        if str(tot).endswith(str(n)) and abs(tot) != abs(n):
            trim_attempt = recurse_pt2(int(re.sub(f"{str(n)}$", "", str(tot))), first_num, reversed_nums[n_idx + 1:])
            if trim_attempt:
                return trim_attempt

        # otherwise try subtracting
        sub_attempt = recurse_pt2(tot - n, first_num, reversed_nums[n_idx+1:])
        return sub_attempt

    return first_num == tot


def solve_pt2(equations):
    score = 0

    for tot, nums in equations:
        original_tot = tot
        first_num = nums[0]
        res = recurse_pt2(tot, first_num, reversed_nums=nums[:0:-1])
        if res:
            score += original_tot

    return score


# PARSE INPUT
input_txt = parse_input()

# PART 1
score = solve_pt1(input_txt)
print(f"Part 1 solution: {score}")


# PART 2
score = solve_pt2(input_txt)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass