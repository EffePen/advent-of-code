

with open("a_input.txt") as f:
    input_txt = f.read()

entrance_pos = None
exit_pos = None
blizzards = []
rows = input_txt.splitlines()
n_rows = len(rows)
n_cols = len(rows[0])

# parse file for blizzards
for r_idx, row in enumerate(rows):
    for c_idx, char in enumerate(row):
        # if first row and not wall, get entrance position
        if r_idx == 0 and char == ".":
            entrance_pos = (r_idx, c_idx)
        #  if last row and not wall, get exit position
        elif r_idx == n_rows - 1 and char == ".":
            exit_pos = (r_idx, c_idx)
        # if blizzard symbol, get position, direction and verse
        elif char in ("<", ">", "^", "v"):
            dir_idx = 0 if char in ("^", "v") else 1
            dir_verse = -1 if char in ("<", "^") else 1
            blizzards.append([[r_idx, c_idx], dir_idx, dir_verse])

positions = [entrance_pos]
time = 0
while exit_pos not in positions:
    # update blizzards
    for b_idx in range(len(blizzards)):
        _, dir_idx, dir_verse = blizzards[b_idx]
        max_idx = n_rows if dir_idx == 0 else n_cols

        # update blizzard pos (the right direction / verse)
        blizzards[b_idx][0][dir_idx] += dir_verse

        # if exceeded boundaries, restart on the other side
        if blizzards[b_idx][0][dir_idx] == 0:
            blizzards[b_idx][0][dir_idx] = max_idx - 2
        elif blizzards[b_idx][0][dir_idx] == max_idx - 1:
            blizzards[b_idx][0][dir_idx] = 1

    blizzard_positions = {tuple(e[0]) for e in blizzards}
    next_positions = []

    # for each current possible position, check the possible next positions
    for r_idx, c_idx in positions:
        for r_inc, c_inc in [[-1, 0], [1, 0], [0, 0], [0, 1], [0, -1]]:
            candidate_next_pos = (r_idx + r_inc, c_idx + c_inc)
            # check if not in blizzard position nor out of border
            if ((candidate_next_pos not in blizzard_positions) and
                    ((0 < candidate_next_pos[0] < n_rows and
                      0 < candidate_next_pos[1] < n_cols)
                     or candidate_next_pos in [entrance_pos, exit_pos])):
                next_positions.append(candidate_next_pos)

    next_positions = set(next_positions)
    positions = next_positions
    assert not blizzard_positions & positions
    time += 1

print(time)

if __name__ == "__main__":
    pass