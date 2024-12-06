

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
                next_dir = curr_dir * rotation
                new_coordinates = (next_pos, next_dir)

                # if repeats a previous pos/dir, it is a loop
                if new_coordinates in seen_coordinates:
                    num_loops += 1
                    break

                seen_coordinates.add(new_coordinates)

                # update direction
                curr_pos = next_pos
                curr_dir = next_dir

            except ValueError:
                break

    return num_loops


def get_block_outgoing_edges(block_pos, block_coordinates):
    edges = []

    # define 90 deg rotation (the Y axis is inverted)
    rotation = 1j

    for curr_dir in [1, -1, 1j, -1j]:
        # get adjacent position
        curr_pos = block_pos - curr_dir
        src = (curr_pos, curr_dir)

        # rotate and check next position (=> the edge)
        next_dir = curr_dir * rotation
        try:
            if next_dir.real:
                # blocks in the same row
                blocks_same_line = [bc for bc in block_coordinates if curr_pos.imag == bc.imag]
                if next_dir == -1:
                    block_ahead = max([bc.real for bc in blocks_same_line if bc.real < curr_pos.real])
                    next_pos = curr_pos.imag * 1j + (block_ahead + 1)
                else:
                    block_ahead = min([bc.real for bc in blocks_same_line if bc.real > curr_pos.real])
                    next_pos = curr_pos.imag * 1j + (block_ahead - 1)

            else:
                # blocks in the same column
                blocks_same_line = [bc for bc in block_coordinates if curr_pos.real == bc.real]
                if next_dir == -1j:
                    block_ahead = max([bc.imag for bc in blocks_same_line if bc.imag < curr_pos.imag])
                    next_pos = curr_pos.real + (block_ahead + 1) * 1j
                else:
                    block_ahead = min([bc.imag for bc in blocks_same_line if bc.imag > curr_pos.imag])
                    next_pos = curr_pos.real + (block_ahead - 1) * 1j
        except ValueError:
            # ends outside the grid
            next_pos = None

        # edge
        dst = (next_pos, next_dir)
        edge = (src, dst)
        edges.append(edge)

    return edges


def get_block_incoming_edges(block_pos, block_coordinates):
    edges = []

    # define 90 deg rotation (the Y axis is inverted)
    rotation = 1j

    for curr_dir in [1, -1, 1j, -1j]:
        # get adjacent position
        curr_pos = block_pos - curr_dir
        dst = (curr_pos, curr_dir)

        # rotate and check prev position (=> the edge)
        prev_dir = curr_dir / rotation
        other_line_pos = curr_pos + prev_dir
        try:
            if curr_dir.real:
                # blocks in the same row
                blocks_same_line = [bc for bc in block_coordinates if other_line_pos.imag == bc.imag]
                if curr_dir == -1:
                    prev_block_pos = min([bc for bc in blocks_same_line if bc.real > other_line_pos.real], key=lambda x: x.real)
                else:
                    prev_block_pos = max([bc for bc in blocks_same_line if bc.real < other_line_pos.real], key=lambda x: x.real)

            else:
                # blocks in the same column
                blocks_same_line = [bc for bc in block_coordinates if other_line_pos.real == bc.real]
                if curr_dir == -1j:
                    prev_block_pos = min([bc for bc in blocks_same_line if bc.imag > other_line_pos.imag], key=lambda x: x.imag)
                else:
                    prev_block_pos = max([bc for bc in blocks_same_line if bc.imag < other_line_pos.imag], key=lambda x: x.imag)
            prev_pos = prev_block_pos - prev_dir

            # edge
            src = (prev_pos, prev_dir)
            edge = (src, dst)
            edges.append(edge)

        except ValueError:
            # starts from outside the grid => skip
            pass

    return edges


def solve_pt2_graph(input_txt, orig_path_coordinates):
    # TODO: explore bug in this alternative solution
    # get initial position and direction
    part_grid, _ = input_txt.split("^")
    init_r_idx = part_grid.count("\n")
    init_c_idx = len(part_grid.split("\n")[-1])
    initial_pos = init_c_idx + init_r_idx * 1j
    initial_dir = -1j

    # get all block coordinates
    block_coordinates = []
    for r_idx, row in enumerate(input_txt.splitlines()):
        block_coordinates += [m.start() + r_idx * 1j for m in re.finditer(re.escape("#"), row)]

    # each block works as an edge between positions around and the block on the right (according to direction)
    edges = []
    for bc in block_coordinates:
        edges += get_block_outgoing_edges(bc, block_coordinates)

    # for each original path coordinates, add the edges that there would be if it was a block
    num_loops = 0
    for idx, opc in enumerate(orig_path_coordinates):
        new_edges = []
        new_edges += get_block_outgoing_edges(opc, block_coordinates)
        new_edges += get_block_incoming_edges(opc, block_coordinates)

        # remove old edges with the same source or destination and get updated set of edges
        updated_edges = edges.copy()
        for ne_src, ne_dst in new_edges:
            updated_edges = [e for e in updated_edges if not (ne_src == e[0])]
        updated_edges += new_edges

        # get initial node (position adjacent to block and direction)
        initial_node_pos = max([bc - initial_dir for bc in block_coordinates + [opc]
                                if bc.real == initial_pos.real and bc.imag < initial_pos.imag], key=lambda x: x.imag)
        initial_node = (initial_node_pos, initial_dir)

        # iterate
        curr_node = initial_node
        seen_nodes = {curr_node}
        while True:
            next_node, = set([e[1] for e in updated_edges if curr_node == e[0]])

            if next_node[0] is None:
                # check if edge leads outside the grid, stop
                break
            elif next_node in seen_nodes:
                # if edge brings to an already visited node, stop and increase the loop count
                num_loops += 1
                break
            else:
                # otherwise update statuses
                curr_node = next_node
                seen_nodes.add(curr_node)
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