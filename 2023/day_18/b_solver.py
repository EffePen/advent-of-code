

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

assert intervals[-1][0][1] == intervals[0][0][0]

n_rows = max_r - min_r + 1
n_cols = max_c - min_c + 1

# translate intervals
intervals = [((s_pos[0] - min_r, s_pos[1] - min_c), (e_pos[0] - min_r, e_pos[1] - min_c))
             for (s_pos, e_pos) in intervals]

# sort intervals by min column index, to allow in/out counting, and then max column index
intervals = sorted(intervals, key=lambda x: (min(x[0][1], x[1][1]), max(x[0][1], x[1][1])))

perimeter_tile_count = sum(abs(e_pos[0] - s_pos[0]) + abs(e_pos[1] - s_pos[1]) for (s_pos, e_pos) in intervals)


# for each grid row, calculate internal blocks
tile_count = 0
r_idx = 0
while r_idx < n_rows:
    inside = False
    start_x = None
    end_x = None
    v_upper_cross = False
    v_lower_cross = False

    # filter only intersecting intervals
    relevant_vertical_intervals = [(s_pos, e_pos) for (s_pos, e_pos) in intervals
                                   if min(s_pos[0], e_pos[0]) <= r_idx <= max(s_pos[0], e_pos[0]) and s_pos[1] == e_pos[1]]

    # get vertical segment common to all relevant intervals => next row
    next_row = min(max(s_pos[0], e_pos[0]) for (s_pos, e_pos) in relevant_vertical_intervals)

    # check if other segments would intersect row before next_row
    other_vertical_start_rows = [(s_pos, e_pos) for (s_pos, e_pos) in intervals
                                 if s_pos[1] == e_pos[1] # vertical
                                 and (s_pos, e_pos) not in relevant_vertical_intervals # not in other intervals
                                 and ((r_idx < min(s_pos[0], e_pos[0]) < next_row) or (r_idx < max(s_pos[0], e_pos[0]) < next_row))
                                 ] # intercepts at least one

    if other_vertical_start_rows:
        next_row = min(next_row, min(min(s_pos[0], e_pos[0]) for (s_pos, e_pos) in other_vertical_start_rows))
    if next_row <= r_idx:
        next_row = r_idx + 1
    r_delta = next_row - r_idx

    # for each row index, check intervals that intersect it
    for (s_pos, e_pos) in relevant_vertical_intervals:
        # Check if already started crossing
        already_crossing = (v_upper_cross or v_lower_cross)

        # Update upper and lower crossing according to current segment
        if min(s_pos[0], e_pos[0]) < r_idx:
            v_upper_cross = True
        if r_idx < max(s_pos[0], e_pos[0]):
            v_lower_cross = True

        started_crossing = (v_upper_cross or v_lower_cross) and not already_crossing
        finished_crossing = (v_upper_cross and v_lower_cross)
        stopped_crossing = already_crossing and not finished_crossing

        # if finished or stopped, reset crossing
        if finished_crossing or stopped_crossing:
            v_upper_cross = False
            v_lower_cross = False

        if not inside:
            # if it was outside and just started crossing, save starting position
            if started_crossing:
                start_x = s_pos[1]
            if stopped_crossing:
                end_x = s_pos[1]
                diameter = end_x - start_x + 1
                tile_count += diameter * r_delta
                start_x = end_x = None
            if finished_crossing:
                inside = True
        elif inside:
            if started_crossing:
                pass
            if stopped_crossing:
                pass
            if finished_crossing:
                inside = False
                end_x = s_pos[1]
                diameter = end_x - start_x + 1
                tile_count += diameter * r_delta
                start_x = end_x = None
        else:
            raise RuntimeError

    # update row
    r_idx = next_row

print(tile_count)

if __name__ == "__main__":
    pass
