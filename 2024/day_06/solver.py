

import re


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    return input_txt


def solve_pt1(input_txt):

    # get initial position and direction
    part_grid, _ = input_txt.split("^")
    init_r_idx = part_grid.count("\n")
    init_c_idx = len(part_grid.split("\n")[-1])
    curr_pos = init_c_idx + init_r_idx * 1j
    curr_dir = -1j

    # grid shape
    grid_h = len(input_txt.splitlines())
    grid_w = len(input_txt.splitlines()[0])

    # define 90 deg rotation (the Y axis is inverted)
    rotation = 1j

    # get all block coordinates
    block_coordinates = []
    for r_idx, row in enumerate(input_txt.splitlines()):
        block_coordinates += [m.start() + r_idx * 1j for m in re.finditer(re.escape("#"), row)]

    seen_coordinates = {curr_pos}
    while True:
        try:
            if curr_dir.real:
                # blocks in the same row
                blocks_same_line = [bc for bc in block_coordinates if curr_pos.imag == bc.imag]
                if curr_dir == -1:
                    block_ahead = max([bc.real for bc in blocks_same_line if bc.real < curr_pos.real])
                    next_pos = curr_pos.imag * 1j + (block_ahead + 1)
                else:
                    block_ahead = min([bc.real for bc in blocks_same_line if bc.real > curr_pos.real])
                    next_pos = curr_pos.imag * 1j + (block_ahead - 1)

            else:
                # blocks in the same column
                blocks_same_line = [bc for bc in block_coordinates if curr_pos.real == bc.real]
                if curr_dir == -1j:
                    block_ahead = max([bc.imag for bc in blocks_same_line if bc.imag < curr_pos.imag])
                    next_pos = curr_pos.real + (block_ahead + 1) * 1j
                else:
                    block_ahead = min([bc.imag for bc in blocks_same_line if bc.imag > curr_pos.imag])
                    next_pos = curr_pos.real + (block_ahead - 1) * 1j

            # get new coordinates
            delta = int(abs(curr_pos - next_pos))
            new_coordinates = [(curr_pos + idx * curr_dir) for idx in range(1, delta + 1)]
            seen_coordinates.update(new_coordinates)

            # update direction
            curr_dir *= rotation
            curr_pos = next_pos

        except ValueError:
            # add final coordinates that lead outside the map
            if curr_dir.real:
                if curr_dir == 1:
                    delta = grid_w - curr_pos.real
                else:
                    delta = curr_pos.real
            else:
                if curr_dir == 1j:
                    delta = grid_h - curr_pos.imag
                else:
                    delta = curr_pos.imag

            new_coordinates = [(curr_pos + idx * curr_dir) for idx in range(1, int(delta))]
            seen_coordinates.update(new_coordinates)

            score = len(seen_coordinates)
            return score, seen_coordinates


def solve_pt2(input_txt, orig_path_coordinates):
    # get initial position and direction
    part_grid, _ = input_txt.split("^")
    init_r_idx = part_grid.count("\n")
    init_c_idx = len(part_grid.split("\n")[-1])
    initial_pos = init_c_idx + init_r_idx * 1j
    initial_dir = -1j

    # define 90 deg rotation (the Y axis is inverted)
    rotation = 1j

    # get all block coordinates
    block_coordinates = []
    for r_idx, row in enumerate(input_txt.splitlines()):
        block_coordinates += [m.start() + r_idx * 1j for m in re.finditer(re.escape("#"), row)]

    num_loops = 0

    for idx, opc in enumerate(orig_path_coordinates):
        # add 1 block
        new_block_coordinates = block_coordinates + [opc]
        curr_pos = initial_pos
        curr_dir = initial_dir

        # iterate anc check for loops
        seen_coordinates = {(curr_pos, curr_dir)}
        while True:
            try:
                if curr_dir.real:
                    # blocks in the same row
                    blocks_same_line = [bc for bc in new_block_coordinates if curr_pos.imag == bc.imag]
                    if curr_dir == -1:
                        block_ahead = max([bc.real for bc in blocks_same_line if bc.real < curr_pos.real])
                        next_pos = curr_pos.imag * 1j + (block_ahead + 1)
                    else:
                        block_ahead = min([bc.real for bc in blocks_same_line if bc.real > curr_pos.real])
                        next_pos = curr_pos.imag * 1j + (block_ahead - 1)

                else:
                    # blocks in the same column
                    blocks_same_line = [bc for bc in new_block_coordinates if curr_pos.real == bc.real]
                    if curr_dir == -1j:
                        block_ahead = max([bc.imag for bc in blocks_same_line if bc.imag < curr_pos.imag])
                        next_pos = curr_pos.real + (block_ahead + 1) * 1j
                    else:
                        block_ahead = min([bc.imag for bc in blocks_same_line if bc.imag > curr_pos.imag])
                        next_pos = curr_pos.real + (block_ahead - 1) * 1j

                # get new coordinates
                delta = int(abs(curr_pos - next_pos))
                new_coordinates = set([((curr_pos + idx * curr_dir), curr_dir) for idx in range(1, delta + 1)])

                # if repeats a previous pos/dir, it is a loop
                if new_coordinates & seen_coordinates:
                    num_loops += 1
                    break

                seen_coordinates.update(new_coordinates)

                # update direction
                curr_dir *= rotation
                curr_pos = next_pos

            except ValueError:
                break

    return num_loops


# PARSE INPUT
input_txt = parse_input()

# PART 1
score, orig_path_coordinates = solve_pt1(input_txt)
print(f"Part 1 solution: {score}")


# PART 2
score = solve_pt2(input_txt, orig_path_coordinates)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass