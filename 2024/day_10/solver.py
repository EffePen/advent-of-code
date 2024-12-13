

def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    grid = {}
    for r_idx, row_txt in enumerate(input_txt.splitlines()):
        for c_idx, c_txt in enumerate(row_txt):
            grid[c_idx + r_idx*1j] = int(c_txt)
    return grid


def solve(grid, part):
    path_starting_pos = [pos for pos in grid if grid[pos] == 0]

    # evolve paths, keeping only distinct (set) of positions for each trail head,
    # since only the distinct final positions count for the score
    current_positions = [(p, head_idx) for head_idx, p in enumerate(path_starting_pos)]
    for next_height in range(1, 10):
        next_positions = list() if part == 2 else set()
        for (curr_pos, head_idx) in current_positions:
            for d in [1, -1, 1j, -1j]:
                next_pos_candidate = curr_pos + d
                if grid.get(next_pos_candidate) == next_height:
                    next_pos = (next_pos_candidate, head_idx)
                    next_positions.append(next_pos) if part == 2 else next_positions.add(next_pos)
        current_positions = next_positions

    score = len(current_positions)

    return score


# PARSE INPUT
input_txt = parse_input()

# PART 1
score = solve(input_txt, part=1)
print(f"Part 1 solution: {score}")


# PART 2
score = solve(input_txt, part=2)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass