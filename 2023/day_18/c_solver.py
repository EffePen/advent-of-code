

with open("a_input.txt") as f:
    input_txt = f.read()


rows = input_txt.splitlines()
direction_map = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
digit_dir_map = {0: "R", 1: "D", 2: "L", 3: "U"}

min_r = min_c = max_r = max_c = 0

intervals = []
starting_pos = (0, 0)
curr_pos = starting_pos
enable_p2 = True
for row in rows:
    if enable_p2:
        _, _, hex_string = row.split()
        length = int(hex_string[2:7], 16)
        digit_dir = int(hex_string[7:8])
        direction = digit_dir_map[digit_dir]
    else:
        direction, length_str, _ = row.split()
        length = int(length_str)

    dir_delta = [e * length for e in direction_map[direction]]
    next_pos = (curr_pos[0] + dir_delta[0], curr_pos[1] + dir_delta[1])
    intervals.append((curr_pos, next_pos))

    curr_pos = next_pos
    min_r = min(min_r, next_pos[0])
    min_c = min(min_c, next_pos[1])
    max_r = max(max_r, next_pos[0])
    max_c = max(max_c, next_pos[1])

# check beginning matches end
assert intervals[-1][0][1] == intervals[0][0][0]

n_rows = max_r - min_r + 1
n_cols = max_c - min_c + 1

# translate intervals
intervals = [((s_pos[0] - min_r, s_pos[1] - min_c), (e_pos[0] - min_r, e_pos[1] - min_c))
             for (s_pos, e_pos) in intervals]

perimeter_tile_count = sum(abs(e_pos[0] - s_pos[0]) + abs(e_pos[1] - s_pos[1]) for (s_pos, e_pos) in intervals)

area = 0
for s_pos, e_pos in intervals:
    x1, y1 = e_pos
    x2, y2 = s_pos
    area += 0.5 * (x1*y2 - x2*y1)

print(area)
print(perimeter_tile_count)
print(area + perimeter_tile_count / 2 + 1)

if __name__ == "__main__":
    pass
