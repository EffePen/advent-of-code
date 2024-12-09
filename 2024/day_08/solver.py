

from collections import defaultdict


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    return input_txt


# TODO: simplify if/else code blocks

def solve_pt1(input_txt):
    rows = input_txt.splitlines()
    grid_h = len(rows)
    grid_w = len(rows[0])

    # get each char coordinates
    char_coordinates = defaultdict(list)
    for r_idx, row in enumerate(rows):
        for c_idx, c in enumerate(row):
            if c != ".":
                char_coordinates[c].append((r_idx, c_idx))

    # for each char group, get char pairs and calculate antinodes
    antinodes = set()
    for c in char_coordinates.keys():
        for r_idx1, c_idx1 in char_coordinates[c]:
            for r_idx2, c_idx2 in char_coordinates[c]:
                if (r_idx1, c_idx1) == (r_idx2, c_idx2):
                    continue

                # each dir distances
                r_idx_diff = abs(r_idx1 - r_idx2)
                c_idx_diff = abs(c_idx1 - c_idx2)

                # check if min-max are crossed
                if ((r_idx1 == max(r_idx1, r_idx2) and c_idx1 == max(c_idx1, c_idx2))
                        or (r_idx1 == min(r_idx1, r_idx2) and c_idx1 == min(c_idx1, c_idx2))):
                    a1_r_idx = min(r_idx1, r_idx2) - r_idx_diff
                    a1_c_idx = min(c_idx1, c_idx2) - c_idx_diff
                    a2_r_idx = max(r_idx1, r_idx2) + r_idx_diff
                    a2_c_idx = max(c_idx1, c_idx2) + c_idx_diff
                else:
                    a1_r_idx = min(r_idx1, r_idx2) - r_idx_diff
                    a1_c_idx = max(c_idx1, c_idx2) + c_idx_diff
                    a2_r_idx = max(r_idx1, r_idx2) + r_idx_diff
                    a2_c_idx = min(c_idx1, c_idx2) - c_idx_diff

                # remove impossible antinodes
                new_antinodes = [(a1_r_idx, a1_c_idx), (a2_r_idx, a2_c_idx)]
                new_antinodes = [a for a in new_antinodes if 0 <= a[0] < grid_h and 0 <= a[1] < grid_w]

                # add new antinodes
                antinodes.update(new_antinodes)

    score = len(antinodes)

    return score


def solve_pt2(input_txt):
    rows = input_txt.splitlines()
    grid_h = len(rows)
    grid_w = len(rows[0])

    # get each char coordinates
    char_coordinates = defaultdict(list)
    for r_idx, row in enumerate(rows):
        for c_idx, c in enumerate(row):
            if c != ".":
                char_coordinates[c].append((r_idx, c_idx))

    # for each char group, get char pairs and calculate antinodes
    antinodes = set()
    for c in char_coordinates.keys():

        if len(char_coordinates[c]) > 1:
            antinodes.update(char_coordinates[c])

        for r_idx1, c_idx1 in char_coordinates[c]:
            for r_idx2, c_idx2 in char_coordinates[c]:
                if (r_idx1, c_idx1) == (r_idx2, c_idx2):
                    continue

                # each dir distances
                r_idx_diff = abs(r_idx1 - r_idx2)
                c_idx_diff = abs(c_idx1 - c_idx2)

                # check if min-max are crossed
                new_antinodes = []
                if ((r_idx1 == max(r_idx1, r_idx2) and c_idx1 == max(c_idx1, c_idx2))
                        or (r_idx1 == min(r_idx1, r_idx2) and c_idx1 == min(c_idx1, c_idx2))):
                    # generate antinode coordinates until out-of-grid
                    # antinodes for side 1
                    idx = 0
                    while True:
                        idx += 1
                        a1_r_idx = min(r_idx1, r_idx2) - idx * r_idx_diff
                        a1_c_idx = min(c_idx1, c_idx2) - idx * c_idx_diff
                        if not (0 <= a1_r_idx < grid_h and 0 <= a1_c_idx < grid_w):
                            break
                        new_antinodes.append((a1_r_idx, a1_c_idx))
                    # antinodes side 2
                    idx = 0
                    while True:
                        idx += 1
                        a2_r_idx = max(r_idx1, r_idx2) + idx * r_idx_diff
                        a2_c_idx = max(c_idx1, c_idx2) + idx * c_idx_diff
                        if not (0 <= a2_r_idx < grid_h and 0 <= a2_c_idx < grid_w):
                            break
                        new_antinodes.append((a2_r_idx, a2_c_idx))
                else:
                    # generate antinode coordinates until out-of-grid
                    # antinodes for side 1
                    idx = 0
                    while True:
                        idx += 1
                        a1_r_idx = min(r_idx1, r_idx2) - idx * r_idx_diff
                        a1_c_idx = max(c_idx1, c_idx2) + idx * c_idx_diff
                        if not (0 <= a1_r_idx < grid_h and 0 <= a1_c_idx < grid_w):
                            break
                        new_antinodes.append((a1_r_idx, a1_c_idx))
                    # antinodes for side 2
                    idx = 0
                    while True:
                        idx += 1
                        a2_r_idx = max(r_idx1, r_idx2) + idx * r_idx_diff
                        a2_c_idx = min(c_idx1, c_idx2) - idx * c_idx_diff
                        if not (0 <= a2_r_idx < grid_h and 0 <= a2_c_idx < grid_w):
                            break
                        new_antinodes.append((a2_r_idx, a2_c_idx))

                # add new antinodes
                antinodes.update(new_antinodes)

    score = len(antinodes)

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