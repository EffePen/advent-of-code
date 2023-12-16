

with open("a_input.txt") as f:
    input_txt = f.read()


def has_one_diff(s1, s2):
    return 1 == sum(x1 != x2 for x1, x2 in zip(s1, s2))


patterns = input_txt.split("\n\n")
scores = []
for pattern in patterns:
    rows = pattern.splitlines()
    n_rows = len(rows)
    add_score = None


    possible_row_idxs = []
    for r_idx in range(0, len(rows)-1):
        if rows[r_idx] == rows[r_idx+1] or has_one_diff(rows[r_idx], rows[r_idx+1]):
            possible_row_idxs.append(r_idx)

    for r_idx in sorted(possible_row_idxs, key=lambda x: abs(x - n_rows / 2)): # sort indices by distance from the center
        max_reflection = min(r_idx+1, n_rows - r_idx - 1)
        p1 = "\n".join(rows[r_idx - max_reflection + 1:r_idx+1])
        p2 = "\n".join(rows[r_idx+1:r_idx + max_reflection + 1][::-1])
        #if p1 == p2 or has_one_diff(p1, p2):
        if has_one_diff(p1, p2):
            add_score = (1+r_idx) * 100
            scores.append(add_score)
            break

    # if a symmetry has been found, stop
    if add_score is not None:
        continue

    # cols
    n_cols = len(rows[0])
    cols = ["".join([rows[r_idx][c_idx] for r_idx in range(n_rows)]) for c_idx in range(n_cols)]

    possible_col_idxs = []
    for c_idx in range(0, len(cols) - 1):
        if cols[c_idx] == cols[c_idx + 1] or has_one_diff(cols[c_idx], cols[c_idx + 1]):
            possible_col_idxs.append(c_idx)

    for c_idx in sorted(possible_col_idxs,
                        key=lambda x: abs(x - n_cols / 2)):  # sort indices by distance from the center
        max_reflection = min(c_idx + 1, n_cols - c_idx - 1)
        p1 = "\n".join(cols[c_idx - max_reflection + 1:c_idx+1])
        p2 = "\n".join(cols[c_idx+1:c_idx + max_reflection + 1][::-1])
        #if p1 == p2 or has_one_diff(p1, p2):
        if has_one_diff(p1, p2):
            add_score = (1 + c_idx)
            scores.append(add_score)
            break

print(sum(scores))

if __name__ == "__main__":
    pass