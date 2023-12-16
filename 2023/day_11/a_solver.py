

with open("a_input.txt") as f:
    input_txt = f.read()


stars_map = {}
space_rows = input_txt.splitlines()
n_rows = len(space_rows)
n_cols = len(space_rows[0])
space_cols = ["".join([space_rows[r_idx][c_idx] for r_idx in range(n_rows)]) for c_idx in range(n_cols)]

# get stars
start_cnt = 1
for r_idx, row in enumerate(space_rows):
    for c_idx, char in enumerate(row):
        if char == "#":
            stars_map[start_cnt] = (r_idx, c_idx)
            start_cnt += 1

# get gap idxs
col_exp_idxs = [c_idx for c_idx, col in enumerate(space_cols) if "#" not in col]
row_exp_idxs = [r_idx for r_idx, row in enumerate(space_rows) if "#" not in row]


stars_list = list(stars_map.values())

score1 = 0
score2 = 0
for s1_idx, s1 in enumerate(stars_list):
    for s2 in stars_list[s1_idx+1:]:
        r1, c1 = s1
        r2, c2 = s2

        num_c_exp = len([c_idx for c_idx in col_exp_idxs if min(c1, c2) < c_idx < max(c1, c2)])
        num_r_exp = len([r_idx for r_idx in row_exp_idxs if min(r1, r2) < r_idx < max(r1, r2)])

        dist1 = abs(r1 - r2) + abs(c1 - c2) + num_c_exp + num_r_exp
        dist2 = abs(r1 - r2) + abs(c1 - c2) + (1000000 - 1) * (num_c_exp + num_r_exp)
        score1 += dist1
        score2 += dist2

print(score1)
print(score2)

if __name__ == "__main__":
    pass
