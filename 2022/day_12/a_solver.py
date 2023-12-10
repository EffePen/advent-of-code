

import string

with open("a_input.txt") as f:
    input_txt = f.read()

# parse heights, start and end position
letter2height = dict(zip(string.ascii_lowercase, range(len(string.ascii_lowercase))))
height_map = []

start_pos = None
end_pos = None
for r_idx, row in enumerate(input_txt.splitlines()):
    # search start pos
    if start_pos is None:
        try:
            start_c_idx = row.index("S")
            start_pos = (r_idx, start_c_idx)
        except:
            pass
    # search end pos
    if end_pos is None:
        try:
            end_c_idx = row.index("E")
            end_pos = (r_idx, end_c_idx)
        except:
            pass
    row = row.replace("S", "a").replace("E", "z")
    height_map.append([letter2height[c] for c in row])

############
n_rows = len(height_map)
n_cols = len(height_map[0])

positions = [start_pos]
possible_moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
already_visited = {start_pos}

steps_cnt = 0
while True:
    next_positions = []

    for pos in positions:
        for move in possible_moves:
            next_r_idx = pos[0] + move[0]
            next_c_idx = pos[1] + move[1]
            next_pos = (next_r_idx, next_c_idx)
            if ((0 <= next_r_idx < n_rows)
                    and (0 <= next_c_idx < n_cols)
                    and (next_pos not in already_visited)
                    and ((height_map[next_pos[0]][next_pos[1]] - height_map[pos[0]][pos[1]]) <= 1)
            ):
                next_positions.append(next_pos)

    already_visited.update(next_positions)

    steps_cnt += 1
    positions = set(next_positions)
    if end_pos in next_positions:
        break

print(steps_cnt)



if __name__ == "__main__":
    pass
