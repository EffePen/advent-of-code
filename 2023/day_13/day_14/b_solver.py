

with open("a_input.txt") as f:
    input_txt = f.read()

rows = input_txt.splitlines()

import re


def tilt(rows, tilt_dir):
    n_rows = len(rows)
    n_cols = len(rows[0])
    cols = ["".join([rows[r_idx][c_idx] for r_idx in range(n_rows)]) for c_idx in range(n_cols)]
    rev_cols = [col[::-1] for col in cols]
    rev_rows = [row[::-1] for row in rows]

    if tilt_dir == "N":
        sequences = rev_cols
    elif tilt_dir == "S":
        sequences = cols
    elif tilt_dir == "W":
        sequences = rev_rows
    elif tilt_dir == "E":
        sequences = rows
    else:
        raise ValueError

    new_sequences = []
    for sequence in sequences:
        # find intervals in which circles can move
        square_idxs = [m.start() for m in re.finditer('#', sequence)]
        intervals = []
        for s_idx in range(len(square_idxs)):
            if s_idx == len(square_idxs) - 1:
                intervals.append((square_idxs[s_idx] + 1, len(sequence)))
            else:
                intervals.append((square_idxs[s_idx] + 1, square_idxs[s_idx+1]))

        if intervals:
            min_idx = min([x0 for x0, x1 in intervals]) - 1 # must not include the first squa
            intervals = [(0, min_idx)] + intervals
        else:
            intervals = [(0, len(sequence))]

        # find circles in interval and move to the extrema
        tmp_score = 0
        new_sequence = []
        for x0, x1 in intervals:
            num_circles = len(list(re.finditer("O", sequence[x0:x1])))
            interval_size = x1 - x0
            for idx in range(interval_size):
                if idx < interval_size - num_circles:
                    new_sequence.append(".")
                else:
                    new_sequence.append("O")
            if x1 < len(sequence):
                new_sequence.append("#")
        assert len(sequence) == len(new_sequence)
        new_sequences.append("".join(new_sequence))

    if tilt_dir == "N":
        rev_cols = new_sequences
        cols = [col[::-1] for col in rev_cols]
        new_rows = ["".join([cols[c_idx][r_idx] for c_idx in range(n_cols)]) for r_idx in range(n_rows)]
    elif tilt_dir == "S":
        cols = new_sequences
        new_rows = ["".join([cols[c_idx][r_idx] for c_idx in range(n_cols)]) for r_idx in range(n_rows)]
    elif tilt_dir == "W":
        rev_rows = new_sequences
        new_rows = [r[::-1] for r in rev_rows]
    elif tilt_dir == "E":
        new_rows = new_sequences
    else:
        raise ValueError

    return new_rows


def calc_north_load(rows):
    n_rows = len(rows)
    n_cols = len(rows[0])
    cols = ["".join([rows[r_idx][c_idx] for r_idx in range(n_rows)]) for c_idx in range(n_cols)]
    rev_cols = [col[::-1] for col in cols]

    scores = []
    for col in rev_cols:
        tmp_score = 0
        for idx in re.finditer("O", col):
            tmp_score += idx.start() + 1

        scores.append(tmp_score)
    return sum(scores)


#debug_scores = [calc_north_load(rows)]

# run cycles until equilibrium
status = "\n".join(rows)
prev_statuses = [status]
for cycle_idx in range(1000000000):
    for d in ["N", "W", "S", "E"]:
        rows = tilt(rows, tilt_dir=d)
    new_status = "\n".join(rows)
    #debug_scores.append(calc_north_load(rows))

    if new_status in prev_statuses:
        prev_identical_idx = prev_statuses.index(new_status)
        last_cycle_start = prev_identical_idx
        cycle_statuses = prev_statuses[prev_identical_idx:]
        break

    prev_statuses.append(new_status)
    # print(new_status + "\n\n\n")

cyclicity = len(cycle_statuses)
final_cycle_idx = (1000000000 - last_cycle_start) % cyclicity
final_cycle_status = cycle_statuses[final_cycle_idx]

# for status in cycle_statuses:
#
#     print(calc_north_load(status.splitlines()))
#     print(status + "\n\n\n")


rows = final_cycle_status.splitlines()

# calculate score
score = calc_north_load(rows)
a = [calc_north_load(s.splitlines()) for s in cycle_statuses]
print(score)


if __name__ == "__main__":
    pass