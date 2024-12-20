

from collections import defaultdict


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    grid = {c_idx + 1j*r_idx: c for r_idx, row in enumerate(input_txt.splitlines())
                                for c_idx, c in enumerate(row)}

    start, = [p for p in grid if grid[p] == "S"]

    road = {p for p in grid if grid[p] != "#"}
    walls = {p for p in grid if grid[p] == "#"}

    path = [start]
    while len(path) < len(road):
        for d in [1, -1, 1j, -1j]:
            new_pos = path[-1] + d
            if new_pos in road and new_pos not in path:
                path.append(new_pos)

    return path, walls


def solve_pt1(path, walls):
    path_dict = {p: p_idx for p_idx, p in enumerate(path)}
    road = set(path)

    cheats = defaultdict(int)
    for wp in walls:
        if {wp+1, wp-1} <= road:
            cheats[abs(path_dict[wp + 1] - path_dict[wp - 1]) - 2] += 1
        if {wp+1j, wp-1j} <= road:
            cheats[abs(path_dict[wp + 1j] - path_dict[wp - 1j]) - 2] += 1

    return sum(cnt for dist, cnt in cheats.items() if dist >= 100)


def solve(path, max_cheat_len=20):
    score = 0
    for p1_idx, p1 in enumerate(path):
        score += len([p2 for p2_idx, p2 in enumerate(path[p1_idx + 102:], start=p1_idx + 102)
                      if abs(p1.real - p2.real) + abs(p1.imag - p2.imag) <= max_cheat_len
                         and p2_idx - p1_idx - (abs(p1.real - p2.real) + abs(p1.imag - p2.imag)) >= 100
                      ])
    return score


# PARSE INPUT
path, walls = parse_input()

# PART 1
score = solve_pt1(path, walls)
print(f"Part 1 solution: {score}")


# PART 2
score = solve(path, max_cheat_len=20)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass