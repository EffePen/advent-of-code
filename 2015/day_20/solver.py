

from collections import defaultdict
from functools import reduce, cache


def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def part1(input_num):
    h_idx = 0
    while True:
        h_idx += 1
        h_factors = factors(h_idx)
        score = sum([f*10 for f in h_factors])
        if score >= input_num:
            return h_idx


def part12_v2(input_num):
    houses_pt1 = defaultdict(lambda: 0)
    houses_pt2 = defaultdict(lambda: 0)
    for i_elf in range(1, input_num // 10):
        for j_house in range(i_elf, input_num // 10, i_elf):
            houses_pt1[j_house] += i_elf
            if j_house < i_elf * 51:
                houses_pt2[j_house] += 1

    # Pt 1 solution
    pt1_sol = None
    for h_idx, h_val in houses_pt1.items():
        if 10 * h_val >= input_num:
            pt1_sol = h_idx
            break

    # Pt 2 solution
    pt2_sol = None
    for h_idx, h_val in houses_pt1.items():
        if 11 * h_val >= input_num:
            pt2_sol = h_idx
            break

    return pt1_sol, pt2_sol


def part2_v2(input_num):
    houses = defaultdict(lambda: 0)

    for i_elf in range(1, input_num // 11 + 1):
        for j_idx in range(50):
            j_house = i_elf + j_idx * i_elf
            houses[j_house] += 11 * i_elf

    for h_idx, h_val in houses.items():
        if h_val >= input_num:
            return h_idx


# input
input_num = 29_000_000

# part 1 & 2
#pt1_sol, pt2_sol = part12_v2(input_num)
#print("Part 1:", pt1_sol)
#print("Part 2:", pt2_sol)
pt2_sol = part2_v2(input_num)
print("Part 2:", pt2_sol)



if __name__ == "__main__":
    pass
