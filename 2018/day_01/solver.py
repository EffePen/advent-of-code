

from collections import defaultdict


def parse_input():
    with open("input.txt") as f:
        lines = f.readlines()
    return [int(l) for l in lines]


def solve_pt2(input_nums):
    num = 0
    prev_nums = {0}

    while True:
        for n in input_nums:
            num += n
            if num in prev_nums:
                return num
            else:
                prev_nums.add(num)


input_nums = parse_input()

# ######## PART 1
cycle_num = sum(input_nums)
print("Part 1 solution: ", cycle_num)


# ######## PART 2
pt2_sol = solve_pt2(input_nums)
print("Part 2 solution: ", pt2_sol)


if __name__ == "__main__":
    pass