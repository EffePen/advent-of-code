

import re

with open("a_input.txt") as f:
    input_txt = f.read()




rows = input_txt.splitlines()


def calc_north_load(rows):
    n_rows = len(rows)
    n_cols = len(rows[0])
    cols = ["".join([rows[r_idx][c_idx] for r_idx in range(n_rows)]) for c_idx in range(n_cols)]
    rev_cols = [col[::-1] for col in cols]

    scores = []
    for col in rev_cols:
        square_idxs = [m.start() for m in re.finditer('#', col)]
        intervals = []
        for s_idx in range(len(square_idxs)):
            if s_idx == len(square_idxs) - 1:
                intervals.append((square_idxs[s_idx] + 1, len(col)))
            else:
                intervals.append((square_idxs[s_idx] + 1, square_idxs[s_idx+1]))

        if intervals:
            min_idx = min([x0 for x0, x1 in intervals]) - 1 # must not include the first squa
            intervals = [(0, min_idx)] + intervals
        else:
            intervals = [(0, len(col))]

        tmp_score = 0
        for x0, x1 in intervals:
            num_circles = len(list(re.finditer("O", col[x0:x1])))
            for circ_tmp_idx in range(num_circles):
                tmp_score += x1 - circ_tmp_idx

        scores.append(tmp_score)
    return sum(scores)


score = calc_north_load(rows)
print(score)

if __name__ == "__main__":
    pass