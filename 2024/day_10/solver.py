

def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    return input_txt


def solve_pt1(input_txt):
    path_starting_pos = []
    grid = {}
    # or each position, set grid integer value and save 0-valued positions
    for r_idx, row_txt in enumerate(input_txt.splitlines()):
        for c_idx, c_txt in enumerate(row_txt):
            height = 100 if c_txt == "." else int(c_txt)
            grid[c_idx + r_idx*1j] = height

            if height == 0:
                path_starting_pos.append(c_idx + r_idx*1j)

    # evolve paths, keeping only distinct (set) of positions for each trail head,
    # since only the distinct final positions count for the score
    current_positions = [(p, head_idx) for head_idx, p in enumerate(path_starting_pos)]
    for next_height in range(1, 10):
        next_positions = set()
        for (curr_pos, head_idx) in current_positions:
            for d in [1, -1, 1j, -1j]:
                next_pos_candidate = curr_pos + d
                if grid.get(next_pos_candidate) == next_height:
                    next_positions.add((next_pos_candidate, head_idx))
        current_positions = next_positions

    score = len(current_positions)

    return score


def solve_pt2(input_txt):
    path_starting_pos = []
    grid = {}
    # or each position, set grid integer value and save 0-valued positions
    for r_idx, row_txt in enumerate(input_txt.splitlines()):
        for c_idx, c_txt in enumerate(row_txt):
            height = 100 if c_txt == "." else int(c_txt)
            grid[c_idx + r_idx*1j] = height

            if height == 0:
                path_starting_pos.append(c_idx + r_idx*1j)

    # evolve paths, keeping all (list) of positions for each trail head,
    # since all the intermediate paths count for the score
    # NOTE: this can be optimized, keeping track of incoming paths and evolving just once per position
    current_positions = [(p, head_idx) for head_idx, p in enumerate(path_starting_pos)]
    for next_height in range(1, 10):
        next_positions = list()
        for (curr_pos, head_idx) in current_positions:
            for d in [1, -1, 1j, -1j]:
                next_pos_candidate = curr_pos + d
                if grid.get(next_pos_candidate) == next_height:
                    next_positions.append((next_pos_candidate, head_idx))
        current_positions = next_positions

    score = len(current_positions)

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