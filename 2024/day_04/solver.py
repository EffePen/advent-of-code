

import re


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    return input_txt


def solve_pt1(input_txt):
    horizontal_text_grid = input_txt.splitlines()

    # HORIZONTAL OCCURRENCES
    h_occurrences = (re.findall("XMAS", "\n".join(horizontal_text_grid)) +
                     re.findall("SAMX", "\n".join(horizontal_text_grid)))

    # VERTICAL OCCURRENCES
    # translate the matrix
    vertical_text_grid = ["".join(zipped_col) for zipped_col in zip(*horizontal_text_grid)]
    v_occurrences = (re.findall("XMAS", "\n".join(vertical_text_grid)) +
                     re.findall("SAMX", "\n".join(vertical_text_grid)))

    # MAIN DIAGONAL OCCURRENCES
    # get grid diagonals
    grid_w = len(horizontal_text_grid[0])
    grid_h = len(horizontal_text_grid)

    diagonal_text_grid = []
    diagonal_starting_coords = []
    diagonal_starting_coords += [(0, c_idx) for c_idx in range(grid_w)]
    diagonal_starting_coords += [(r_idx, 0) for r_idx in range(1, grid_h)]

    for (r_idx, c_idx) in diagonal_starting_coords:
        d_text_row = []
        while (0 <= c_idx < grid_w) and (0 <= r_idx < grid_h):
            d_text_row.append(horizontal_text_grid[r_idx][c_idx])
            c_idx += 1
            r_idx += 1
        diagonal_text_grid.append("".join(d_text_row))

    md_occurrences = (re.findall("XMAS", "\n".join(diagonal_text_grid)) +
                      re.findall("SAMX", "\n".join(diagonal_text_grid)))

    # SECONDARY DIAGONAL OCCURRENCES
    # get grid diagonals
    grid_w = len(horizontal_text_grid[0])
    grid_h = len(horizontal_text_grid)

    sd_text_grid = []
    diagonal_starting_coords = []
    diagonal_starting_coords += [(0, c_idx) for c_idx in range(grid_w)]
    diagonal_starting_coords += [(r_idx, grid_w-1) for r_idx in range(1, grid_h)]

    for (r_idx, c_idx) in diagonal_starting_coords:
        d_text_row = []
        while (0 <= c_idx < grid_w) and (0 <= r_idx < grid_h):
            d_text_row.append(horizontal_text_grid[r_idx][c_idx])
            c_idx -= 1
            r_idx += 1
        sd_text_grid.append("".join(d_text_row))

    sd_occurrences = (re.findall("XMAS", "\n".join(sd_text_grid)) +
                      re.findall("SAMX", "\n".join(sd_text_grid)))

    score = len(h_occurrences + md_occurrences + sd_occurrences + v_occurrences)

    return score


def solve_pt2(input_txt):
    horizontal_text_grid = input_txt.splitlines()

    # Define the 4 possible X-MAX patterns
    patterns = [
        r"M.M\n.A.\nS.S",
        r"M.S\n.A.\nM.S",
        r"S.M\n.A.\nS.M",
        r"S.S\n.A.\nM.M",
    ]

    grid_w = len(horizontal_text_grid[0])
    grid_h = len(horizontal_text_grid)

    # check 3x3 patches for the patterns
    score = 0
    for r_idx in range(grid_h - 2):
        for c_idx in range(grid_w - 2):
            patch_grid = [horizontal_text_grid[i][c_idx:c_idx+3] for i in range(r_idx, r_idx+3)]
            patch_txt = "\n".join(patch_grid)
            ok = any([re.match(p, patch_txt) for p in patterns])
            if ok:
                score += 1
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