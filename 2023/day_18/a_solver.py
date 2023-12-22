

with open("a_input.txt") as f:
    input_txt = f.read()

# 57296
rows = input_txt.splitlines()
direction_map = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

min_r = min_c = max_r = max_c = 0

intervals = []
starting_pos = (0, 0)
curr_pos = starting_pos
for row in rows:
    direction, length_str, color = row.split()
    dir_delta = [e * int(length_str) for e in direction_map[direction]]
    next_pos = (curr_pos[0] + dir_delta[0], curr_pos[1] + dir_delta[1])
    intervals.append(((curr_pos, next_pos), color))

    curr_pos = next_pos
    min_r = min(min_r, next_pos[0])
    min_c = min(min_c, next_pos[1])
    max_r = max(max_r, next_pos[0])
    max_c = max(max_c, next_pos[1])

assert intervals[-1][0][1] == intervals[0][0][0]

n_rows = max_r - min_r + 1
n_cols = max_c - min_c + 1

# translate intervals
intervals = [(((s_pos[0] - min_r, s_pos[1] - min_c), (e_pos[0] - min_r, e_pos[1] - min_c)), color)
             for ((s_pos, e_pos), color) in intervals]

# sort intervals by min column index, to allow in/out counting, and then max column index
intervals = sorted(intervals, key=lambda x: (min(x[0][0][1], x[0][1][1]), max(x[0][0][1], x[0][1][1])))

perimeter_tile_count = sum(abs(e_pos[0] - s_pos[0]) + abs(e_pos[1] - s_pos[1]) for ((s_pos, e_pos), _) in intervals)

grid = [["." for _ in range(n_cols)] for _ in range(n_rows)]

for ((s_pos, e_pos), color) in intervals:
    for r_idx in range(min(s_pos[0], e_pos[0]), max(s_pos[0], e_pos[0]) + 1):
        for c_idx in range(min(s_pos[1], e_pos[1]), max(s_pos[1], e_pos[1]) + 1):
            grid[r_idx][c_idx] = "#"


grid_str = "\n".join(["".join(row) for row in grid])
with open("tmp_view1.txt", "w") as f:
    f.write(grid_str)

# for each grid row, calculate internal blocks
tile_count = 0
for r_idx in range(n_rows):
    inside = False
    start_x = None
    end_x = None
    v_upper_cross = False
    v_lower_cross = False

    # filter only intersecting intervals
    relevant_intervals = [((s_pos, e_pos), color) for ((s_pos, e_pos), color) in intervals
                          if min(s_pos[0], e_pos[0]) <= r_idx <= max(s_pos[0], e_pos[0]) and s_pos[1] == e_pos[1]]

    # for each row index, check intervals that intersect it
    for ((s_pos, e_pos), color) in relevant_intervals:
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
                tile_count += diameter
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
                tile_count += diameter
                start_x = end_x = None
        else:
            raise RuntimeError

print(tile_count)

if __name__ == "__main__":
    pass
