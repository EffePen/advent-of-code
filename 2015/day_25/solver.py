

import re


def parse_input():
    with open("input.txt") as f:
        (r_idx_str, c_idx_str), = re.findall("row ([0-9]+), column ([0-9]+)", f.read())
        r_idx_str, c_idx_str = int(r_idx_str), int(c_idx_str)
    return r_idx_str, c_idx_str


def part1(r_idx, c_idx):
    # calculating the number of the code
    # tot_rows + 1 = r_idx + c_idx => tot_rows = r_idx + c_idx -1
    tot_rows = r_idx + c_idx - 1
    num_cells_last_full_triangle = tot_rows * (tot_rows - 1) // 2
    num_cells_next_line = tot_rows - r_idx + 1
    num_codes = num_cells_last_full_triangle + num_cells_next_line

    code = 20151125
    for _ in range(num_codes - 1):
        code = (code * 252533) % 33554393
    return code


# input
r_idx, c_idx = parse_input()

# part 1
code = part1(r_idx, c_idx)
print("Part 1:", code)


if __name__ == "__main__":
    pass
