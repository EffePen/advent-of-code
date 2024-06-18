

import collections


def parse_input():
    with open("input.txt") as f:
        map_rows = f.read().splitlines()
    map = collections.defaultdict(lambda: collections.defaultdict(lambda: " "))
    for r_idx, map_row in enumerate(map_rows):
        for c_idx, c in enumerate(map_row):
            map[r_idx][c_idx] = c
    return map


def traverse_map(map):
    letters = []

    curr_c = list(map[0].values()).index("|")
    curr_coords = (0, curr_c)
    curr_dir = "|"
    seen = {"|": set(), "-": set()}
    n_steps = 0

    while True:
        # update seen coordinates in current direction
        seen[curr_dir].add(curr_coords)
        n_steps += 1

        # get possible next coords
        curr_r, curr_c = curr_coords
        if curr_dir == "|":
            next_coords = {(curr_r + 1, curr_c), (curr_r - 1, curr_c)}
        elif curr_dir == "-":
            next_coords = {(curr_r, curr_c + 1), (curr_r, curr_c - 1)}
        else:
            raise ValueError

        # remove seen coords, out-of-grid coords, and empy coords. Only one pair should remain
        next_coords = next_coords - seen[curr_dir]
        next_coords = {nc for nc in next_coords if map[nc[0]][nc[1]] != " "}

        # if there are no next coords, exit the loop
        if not next_coords:
            break

        # otherwise adjust direction according to
        (next_r, next_c), = next_coords
        next_symbol = map[next_r][next_c]
        if next_symbol == "+":
            curr_dir = "|" if curr_dir == "-" else "-"
        elif next_symbol not in ("|", "-"):
            letters.append(next_symbol)
        curr_coords = (next_r, next_c)

    return "".join(letters), n_steps


map = parse_input()


# ######## PART 1 & 2
letters, n_steps = traverse_map(map)
print("Part 1 solution: ", letters)
print("Part 2 solution: ", n_steps)


if __name__ == "__main__":
    pass