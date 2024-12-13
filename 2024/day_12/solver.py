
from collections import defaultdict


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    grid = {}
    for r_idx, row in enumerate(input_txt.splitlines()):
        for c_idx, c in enumerate(row):
            grid[c_idx + r_idx * 1j] = c
    return grid


def solve(grid, part):
    seen_positions = set()
    areas = defaultdict(int)
    perimeters = defaultdict(list)

    group_idx = 0

    for initial_pos, plant_type in grid.items():
        if initial_pos in seen_positions:
            continue

        # start a new region exploration
        group_idx += 1
        curr_positions = {initial_pos}
        while curr_positions:
            curr_pos = curr_positions.pop()
            seen_positions.add(curr_pos)
            areas[(group_idx, plant_type)] += 1

            # check if neighbors are of the same type
            for delta in [1, -1, 1j, -1j]:
                cnp = curr_pos + delta
                # not on grid or different plant type: save perimeter position and clockwise direction
                if grid.get(cnp) != plant_type:
                    perimeters[(group_idx, grid[curr_pos])].append((cnp, delta * 1j))
                # same plant type and not seen before: add for further exploration
                elif cnp not in seen_positions:
                    curr_positions.add(cnp)

    score = 0
    for group_id in areas.keys():
        # to count edges in perimeter, evolve perimeter positions along direction and diff
        num_lines = len(set(perimeters[group_id]) - set([(p+d, d) for p, d in perimeters[group_id]]))
        area = areas[group_id]
        price = area * (num_lines if part == 2 else len(perimeters[group_id]))
        score += price

    return score


# PARSE INPUT
grid = parse_input()

# PART 1
score = solve(grid, part=1)
print(f"Part 1 solution: {score}")


# PART 2
score = solve(grid, part=2)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass