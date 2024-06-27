

def parse_input():
    with open("input.txt") as f:
        initial_map = f.read().splitlines()

    n_rows = len(initial_map)
    n_cols = len(initial_map[0])
    if n_rows % 2 == 0 or n_cols % 2 == 0:
        raise ValueError("Initial map must have an odd number of cols and rows")

    infection_map = {}
    mid_y = n_rows // 2
    mid_x = n_cols // 2
    for x in range(n_cols):
        for y in range(n_rows):
            coord = (x - mid_x) + 1j * (y - mid_y)
            infection_map[coord] = 0 if initial_map[y][x] == "." else 2
    return infection_map


def evolve(infection_map, initial_pos, initial_dir, n_iterations, pt=1):
    status_step = 2 if pt == 1 else 1
    rotation_map = {0: -1j, 1: 1, 2: 1j, 3: -1}
    count = 0
    curr_pos = initial_pos
    curr_dir = initial_dir
    for _ in range(n_iterations):
        curr_status = infection_map.get(curr_pos, 0)
        curr_dir = curr_dir * rotation_map[curr_status]
        infection_map[curr_pos] = (curr_status + status_step) % 4
        if infection_map[curr_pos] == 2:
            count += 1
        curr_pos += curr_dir
    return count


# ######## PART 1
infection_map = parse_input()
initial_pos = 0
initial_dir = -1j
n_iterations = 10_000
count = evolve(infection_map, initial_pos, initial_dir, n_iterations, pt=1)
print("Part 1 solution: ", count)


# ######## PART 2
infection_map = parse_input()
initial_pos = 0
initial_dir = -1j
n_iterations = 10_000_000
count = evolve(infection_map, initial_pos, initial_dir, n_iterations, pt=2)
print("Part 2 solution: ", count)


if __name__ == "__main__":
    pass