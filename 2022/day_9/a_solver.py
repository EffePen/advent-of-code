

with open("a_input.txt") as f:
    input_txt = f.read()


h_curr_pos = [0, 0]
t_curr_pos = [0, 0]
t_pos_hst = [tuple(t_curr_pos)]
for move in input_txt.splitlines():
    direction, dist = move.split()
    move_dir_idx = 0 if direction in ("R", "L") else 1
    move_dir_verse = 1 if direction in ("R", "D") else -1

    for _ in range(int(dist)):
        # update head pos
        h_curr_pos[move_dir_idx] += move_dir_verse
        if not ((h_curr_pos[0]-1 <= t_curr_pos[0] <= h_curr_pos[0]+1) and
                (h_curr_pos[1] - 1 <= t_curr_pos[1] <= h_curr_pos[1] + 1)):
            # update tail col pos
            for dir_idx in (0, 1):
                if h_curr_pos[dir_idx] > t_curr_pos[dir_idx]:
                    t_curr_pos[dir_idx] += 1
                elif h_curr_pos[dir_idx] < t_curr_pos[dir_idx]:
                    t_curr_pos[dir_idx] -= 1

            t_pos_hst.append(tuple(t_curr_pos))

print(len(set(t_pos_hst)))

if __name__ == "__main__":
    pass