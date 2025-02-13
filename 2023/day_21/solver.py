
import math


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


def solve_p2(grid, num_steps):
    score = 0
    start, = [pos for pos in grid if grid[pos] == "S"]

    # create a 3x3 grid
    grid_w = int(max([p.real for p in grid])) + 1
    grid_h = int(max([p.imag for p in grid])) + 1
    grid_3x3 = dict()
    for rx_idx in (-1, 0, 1, -2, +2):
        for ry_idx in (-1, 0, 1, -2, +2):
            replica_grid = {p + (rx_idx * grid_w) + (ry_idx * grid_h)*1j: e for p, e in grid.items()}
            grid_3x3.update(replica_grid)

    # run djikstra on 3x3 replica grid
    current_positions = {start}
    visited = {start: 0}
    while current_positions:
        curr_pos = current_positions.pop()
        dist = visited[curr_pos]
        next_positions = {curr_pos + d for d in [1, -1, 1j, -1j]
                          if grid_3x3.get(curr_pos + d, "#") != "#"
                          and visited.get(curr_pos + d, math.inf) > dist + 1}
        visited.update({p: dist+1 for p in next_positions})
        current_positions.update(next_positions)

    # for each neighboring replica, get the first touched tile
    replica_info = {}
    for rx_idx in (-1, 0, 1, -2, +2):
        for ry_idx in (-1, 0, 1, -2, +2):
            replica_grid = {p + (rx_idx * grid_w) + (ry_idx * grid_h)*1j: e for p, e in grid.items()}
            min_p, min_dist = min([(p, visited[p]) for p in replica_grid if p in visited], key=lambda x: x[1])
            _, max_dist = max([(p, visited[p]) for p in replica_grid if p in visited], key=lambda x: x[1])
            num_even = len([(p, visited[p]) for p in replica_grid if visited.get(p, math.inf) % 2 == 0])
            num_odd = len([(p, visited[p]) for p in replica_grid if visited.get(p, math.inf) % 2 == 1])
            replica_info[(rx_idx, ry_idx)] = (min_p - rx_idx * grid_w - ry_idx * grid_h * 1j, min_dist, max_dist - min_dist, num_even, num_odd)

    a = 1

    return score







# PARSE INPUT
grid, grid_map = parse_input()

# PART 1
score = solve_p1(grid_map, num_steps=64)
print("Part 1 solution:", score)

# PART 2
score = solve_p2(grid_map, num_steps=64)
print("Part 2 solution:", score)


if __name__ == "__main__":
    pass
