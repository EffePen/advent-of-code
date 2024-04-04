

def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    first_row = input_txt
    return first_row


first_row = parse_input()
trap_masks = [
    "^^.",
    ".^^",
    "^..",
    "..^",
]


# PART 1
rows = [first_row]
while len(rows) < 40:
    last_row = '.' + rows[-1] + '.'
    new_row = ''.join(['^' if last_row[idx-1:idx+2] in trap_masks else '.' for idx in range(1, len(first_row) + 1)])
    rows.append(new_row)
floor_map = '\n'.join(rows)
num_safe_tiles = floor_map.count('.')

print(f"Part 1 solution: {num_safe_tiles}")

# PART 2
tot_n_rows_pt2 = 400000
rows = [first_row]
while len(rows) < tot_n_rows_pt2:
    last_row = '.' + rows[-1] + '.'
    new_row = ''.join(['^' if last_row[idx-1:idx+2] in trap_masks else '.' for idx in range(1, len(first_row) + 1)])
    if new_row != first_row:
        rows.append(new_row)
    else:
        break

periodicity = len(rows)
num_periods = tot_n_rows_pt2 // periodicity
remainder_rows = tot_n_rows_pt2 % periodicity
periodic_safe_tiles = '\n'.join(rows).count('.')
remainder_safe_tiles = '\n'.join(rows[:remainder_rows]).count('.')
num_safe_tiles = periodic_safe_tiles * num_periods + remainder_safe_tiles

print(f"Part 2 solution: {num_safe_tiles}")


if __name__ == "__main__":
    pass