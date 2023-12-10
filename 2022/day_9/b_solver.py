

with open("a_input.txt") as f:
    input_txt = f.read()


n_knots = 10
knots_pos = [[0, 0] for _ in range(n_knots)]

t_pos_hst = [tuple(knots_pos[-1])]

for move in input_txt.splitlines():
    direction, dist = move.split()
    move_dir_idx = 0 if direction in ("R", "L") else 1
    move_dir_verse = 1 if direction in ("R", "D") else -1

    for _ in range(int(dist)):
        # update head pos
        knots_pos[0][move_dir_idx] += move_dir_verse
        h_curr_pos = knots_pos[0]

        # update all following
        for knot_idx in range(1, n_knots):
            prev_knot_pos = knots_pos[knot_idx-1]
            if not ((prev_knot_pos[0]-1 <= knots_pos[knot_idx][0] <= prev_knot_pos[0]+1) and
                    (prev_knot_pos[1] - 1 <= knots_pos[knot_idx][1] <= prev_knot_pos[1] + 1)):
                # update tail col pos
                for dir_idx in (0, 1):
                    if prev_knot_pos[dir_idx] > knots_pos[knot_idx][dir_idx]:
                        knots_pos[knot_idx][dir_idx] += 1
                    elif prev_knot_pos[dir_idx] < knots_pos[knot_idx][dir_idx]:
                        knots_pos[knot_idx][dir_idx] -= 1

        t_pos_hst.append(tuple(knots_pos[-1]))

print(len(set(t_pos_hst)))

if __name__ == "__main__":
    pass