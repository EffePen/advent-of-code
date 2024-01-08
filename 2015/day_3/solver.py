
def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    return input_txt

input_txt = parse_input()

# part 1
prev_coords = (0, 0)
visited_coords_p1 = {prev_coords}
for c in input_txt:
    if c == ">":
        next_coords = (prev_coords[0], prev_coords[1] + 1)
    elif c == "<":
        next_coords = (prev_coords[0], prev_coords[1] - 1)
    elif c == "^":
        next_coords = (prev_coords[0] - 1, prev_coords[1])
    elif c == "v":
        next_coords = (prev_coords[0] + 1, prev_coords[1])
    else:
        raise RuntimeError

    visited_coords_p1.add(next_coords)
    prev_coords = next_coords

print("Part 1:", len(visited_coords_p1))


# part 2
prev_coords_list = [(0, 0), (0, 0)]
visited_coords_p2 = set(prev_coords_list)
for c_idx, c in enumerate(input_txt):
    s_idx = c_idx % 2
    prev_coords = prev_coords_list[s_idx]

    if c == ">":
        next_coords = (prev_coords[0], prev_coords[1] + 1)
    elif c == "<":
        next_coords = (prev_coords[0], prev_coords[1] - 1)
    elif c == "^":
        next_coords = (prev_coords[0] - 1, prev_coords[1])
    elif c == "v":
        next_coords = (prev_coords[0] + 1, prev_coords[1])
    else:
        raise RuntimeError

    visited_coords_p2.add(next_coords)
    prev_coords_list[s_idx] = next_coords

print("Part 2:", len(visited_coords_p2))


if __name__ == "__main__":
    pass
