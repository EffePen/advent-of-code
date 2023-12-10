
import re

with open("a_input.txt") as f:
    input_txt = f.read()
rows = input_txt.splitlines()

# get starting pos
start_pos = None
for r_idx, row in enumerate(rows):
    c_idx = row.find("S")
    if c_idx != -1:
        start_pos = (r_idx, c_idx)
        break

reverse_dir = {"w": "e", "e": "w", "n": "s", "s": "n"}

dir_dict = {"n": (-1, 0), "s": (1, 0), "w": (0, -1), "e": (0, 1)}

pipes_dict = {
    "|": ("n", "s"),
    "-": ("e", "w"),
    "L": ("n", "e"),
    "J": ("n", "w"),
    "7": ("s", "w"),
    "F": ("s", "e"),
    ".": (),
}

paths = [[(start_pos, "n")],
         [(start_pos, "s")],
         [(start_pos, "w")],
         [(start_pos, "e")]]


checked_positions = []

while len(checked_positions) == len(set(checked_positions)):
    for p_idx, path in enumerate(paths):
        if not path[-1]:
            continue

        last_pos, last_dir = path[-1]
        next_pos = (last_pos[0] + dir_dict[last_dir][0],
                    last_pos[1] + dir_dict[last_dir][1])

        if not ((0 <= next_pos[0] < len(rows))
                and (0 <= next_pos[1] < len(rows[0]))):
            paths[p_idx].append(None)
            continue

        # get next pipe, if any
        next_pipe = rows[next_pos[0]][next_pos[1]]
        rev_dir = reverse_dir[last_dir]

        # get next direction if any
        next_pipe_dirs = pipes_dict[next_pipe]
        if rev_dir not in next_pipe_dirs:
            paths[p_idx].append(None)
            continue
        next_dir, = [d for d in next_pipe_dirs if d != rev_dir]

        paths[p_idx].append((next_pos, next_dir))
        checked_positions.append(next_pos)


loop_positions = None
for p1_idx, path1 in enumerate(paths):
    for path2 in paths[p1_idx+1:]:
        if path1[-1] is None or path2[-1] is None:
            continue
        if path1[-1][0] == path2[-1][0]:
            # remove ends from second part
            loop_positions = [p for p, d in path1 + path2[1:-1][::-1]]

print(len(loop_positions) / 2)


# search area
start_pos = loop_positions[0]
start_neighbors_pos = [loop_positions[-1], loop_positions[1]]
start_dirs = []
for start_neighbor_pos in start_neighbors_pos:
    if start_neighbor_pos[0] == start_pos[0]:
        if start_neighbor_pos[1] > start_pos[1]:
            start_dirs.append("s")
        else:
            start_dirs.append("n")
    elif start_neighbor_pos[0] > start_pos[0]:
        start_dirs.append("e")
    else:
        start_dirs.append("w")

loop_dirs = [start_dirs] + [pipes_dict[rows[r_idx][c_idx]] for r_idx, c_idx in loop_positions[1:]]


inside_count = 0
for r_idx, row in enumerate(rows):
    crossing_count = 0
    contiguous_v_dirs = set()

    for c_idx in range(len(row)):
        pos = (r_idx, c_idx)

        # check if is loop and its index
        try:
            loop_index = loop_positions.index(pos)
            # get only vertical directions for this pipe
            v_dirs = set(loop_dirs[loop_index]) & {"n", "s"}
        except ValueError:
            loop_index = None
            v_dirs = None

        # if it is not a loop element, add 1 to inside count if it crossed the loop an odd number of times
        if loop_index is None:
            is_inside = crossing_count % 2 != 0
            inside_count += 1 if is_inside else 0
        else:
            # if this pipe has vertical directions
            if v_dirs:
                # if crossed north/south, increase crossing and clear prev v dirs
                if (v_dirs | contiguous_v_dirs) == {"n", "s"}:
                    crossing_count += 1
                    contiguous_v_dirs = set()
                # if not, but already started crossing, clear prev v dirs (it never crossed)
                elif contiguous_v_dirs:
                    contiguous_v_dirs = set()
                # if not but just started crossing, update v dirs
                else:
                    contiguous_v_dirs = v_dirs

print(inside_count)

if __name__ == "__main__":
    pass
