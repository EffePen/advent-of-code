

with open("a_input.txt") as f:
    input_txt = f.read()


rows = input_txt.splitlines()


def apply_mirror(position, velocity, mirror_symbol):
    # apply mirror to velocity
    if mirror_symbol in ("\\", "/"):
        if mirror_symbol == "/":
            velocity = (-velocity[0], -velocity[1])
        next_velocities = [(velocity[1], velocity[0])]
    elif mirror_symbol == "|" and velocity[1] != 0:
        next_velocities = [(-1, 0), (1, 0)]
    elif mirror_symbol == "-" and velocity[0] != 0:
        next_velocities = [(0, -1), (0, 1)]
    else:
        next_velocities = [velocity]

    # get final positions based on final velocities
    next_positions = [(position[0] + v[0], position[1] + v[1]) for v in next_velocities]

    return next_positions, next_velocities


def simulate_beams(starting_pos, starting_vel, rows):
    curr_beams = [(starting_pos, starting_vel)]
    past_beams_map = {(0, 0): [(0, 1)]}
    n_rows = len(rows)
    n_cols = len(rows[0])

    while curr_beams:
        next_beams = []
        for pos, vel in curr_beams:
            mirror = rows[pos[0]][pos[1]]
            next_positions, next_velocities = apply_mirror(pos, vel, mirror_symbol=mirror)

            for next_pos, next_vel in zip(next_positions, next_velocities):
                # if next position not on grid, skip
                if not ((0 <= next_pos[0] < n_rows) and (0 <= next_pos[1] < n_cols)):
                    continue

                # update beams that have been already considered
                if next_pos not in past_beams_map:
                    past_beams_map[next_pos] = []

                if next_vel not in past_beams_map[next_pos]:
                    past_beams_map[next_pos].append(next_vel)
                    next_beams.append((next_pos, next_vel))

        curr_beams = next_beams
    return past_beams_map


# part 1
past_beams_map = simulate_beams(starting_pos=(0, 0), starting_vel=(0, 1), rows=rows)
print(len(past_beams_map))

# part 2
n_rows = len(rows)
n_cols = len(rows[0])
num_energized = []

assert n_rows == n_cols
square_side = n_rows

# top left side
for s_idx in range(square_side):
    for starting_vel in [(0, 1), (1, 0)]:
        if starting_vel[1] != 0:
            starting_pos = (s_idx, 0)
        else:
            starting_pos = (0, s_idx)
        past_beams_map = simulate_beams(starting_pos=starting_pos, starting_vel=starting_vel, rows=rows)
        num_energized.append(len(past_beams_map))


# top bottom right
for s_idx in range(square_side):
    for starting_vel in [(0, -1), (-1, 0)]:
        if starting_vel[1] != 0:
            starting_pos = (square_side - s_idx - 1, 0)
        else:
            starting_pos = (0, square_side - s_idx - 1)
        past_beams_map = simulate_beams(starting_pos=starting_pos, starting_vel=starting_vel, rows=rows)
        num_energized.append(len(past_beams_map))

print(max(num_energized))


if __name__ == "__main__":
    pass
