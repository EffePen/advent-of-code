
import math


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    blocks = [int(coords_txt.split(",")[0]) + 1j*int(coords_txt.split(",")[1]) for coords_txt in input_txt.splitlines()]
    return blocks


def solve_pt1(blocks, grid_size=71, num_sim=1024, end_stops=False):
    visited = dict()
    start = 0
    grid = {c_idx + 1j*r_idx: "."
            for r_idx in range(grid_size) for c_idx in range(grid_size) if c_idx + 1j*r_idx not in blocks[:num_sim]}
    end = (grid_size - 1) + 1j*(grid_size - 1)
    curr_statuses = {(start, 0)}
    end_values = list()

    while curr_statuses:
        p, v = curr_statuses.pop()
        if visited.get(p, math.inf) < v or p not in grid:
            continue
        if p == end:
            end_values.append(v)
            if end_stops:
                return True
        visited[p] = v
        curr_statuses.update([(p+d, v+1) for d in [1, -1, 1j, -1j]])
    score = None if not end_values else min(end_values)
    return score


def solve_pt2(blocks, grid_size=71):
    # binary search
    num_blocks = len(blocks)
    search_intervals = [(0, num_blocks)]
    while search_intervals:
        si = search_intervals.pop()
        if (si[1] - si[0]) <= 1:
            return f"{int(blocks[si[1]].real)},{int(blocks[si[1]].imag)}"
        middle_point = (si[1] - (si[1] - si[0]) // 2)
        csi1, csi2 = (si[0], middle_point), (middle_point, si[1])

        res = solve_pt1(blocks, grid_size=grid_size, num_sim=middle_point+1, end_stops=True)
        if res is None:
            search_intervals.append(csi1)
        else:
            search_intervals.append(csi2)


# PARSE INPUT
blocks = parse_input()

# PART 1
score = solve_pt1(blocks)
print(f"Part 1 solution: {score}")


# PART 2
score = solve_pt2(blocks)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass