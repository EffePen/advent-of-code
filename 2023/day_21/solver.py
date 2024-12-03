
import re


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()

    grid = input_txt.splitlines()
    grid_map = {}
    # use complex numbers to indicate coords in the 2d plane
    for r_idx, row in enumerate(grid):
        for c_idx, c in enumerate(row):
            grid_map[r_idx * 1j + c_idx] = c

    return grid, grid_map


def solve_p1(grid_map, num_steps):
    grid_coords = set(grid_map.keys())

    start_coords, = [coords for coords, elem in grid_map.items() if elem == "S"]
    new_coords = {start_coords}

    # prepare seen coords according to step parity
    seen_coords = {}
    seen_coords[False] = set()
    seen_coords[True] = new_coords

    # run iterations
    parity = True
    for _ in range(num_steps):
        # switch parity
        parity = not parity

        # evolve each new coordinate in the 4 directions
        candidate_new_coords = []
        for nc in new_coords:
            candidate_new_coords += [nc + d for d in [1, -1, 1j, -1j]]

        # select only unique ones, and remove those that have been seen before, or are not available, or are not on the grid
        candidate_new_coords = (set(candidate_new_coords) & grid_coords) - seen_coords[parity]
        new_coords = [cnc for cnc in candidate_new_coords if grid_map[cnc] != "#"]

        # add them to the seen ones for current parity
        seen_coords[parity].update(new_coords)

    return len(seen_coords[parity])


# PARSE INPUT
grid, grid_map = parse_input()

# PART 1
score = solve_p1(grid_map, num_steps=64)
print("Part 1 solution:", score)


if __name__ == "__main__":
    pass
