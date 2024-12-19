
import math


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    grid = {c_idx + 1j*r_idx: c for r_idx, row in enumerate(input_txt.splitlines())
                                for c_idx, c in enumerate(row) if c != "#"}
    return grid


def solve(grid, part):
    start, = [p for p in grid if grid[p] == "S"]
    end, = [p for p in grid if grid[p] == "E"]

    # find distances of (position, direction) with djikstra
    visited = dict()
    curr_statuses = {(start, +1, 0)} # (position, direction, distance)
    while curr_statuses:
        p, d, v = curr_statuses.pop()
        if visited.get((p, d), math.inf) < v or p not in grid:
            continue
        visited[(p, d)] = v
        curr_statuses.update([(p+d, d, v+1), (p+d*1j, d*1j, v+1001), (p+d*-1j, d*-1j, v+1001), (p-d, -d, v+2001)])
    best_score = min([v for (p, _), v in visited.items() if p == end])

    if part == 1:
        return best_score
    else: # reverse path and check compatible (position, direction) distances seen before
        tiles = {end}
        curr_statuses = set([(p, d, v) for (p, d), v in visited.items() if p == end and v == best_score])
        while curr_statuses:
            p, d, v = curr_statuses.pop()
            p -= d
            candidate_next_statues = [(p, d, v-1), (p, d*-1j, v-1001), (p, d*1j, v-1001), (p, -d, v-2001)]
            candidate_next_statues = [cns for cns in candidate_next_statues if cns[2] == visited.get((cns[0], cns[1]), math.inf)]
            tiles.update([cns[0] for cns in candidate_next_statues])
            curr_statuses.update(candidate_next_statues)
        return len(tiles)


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