

def parse_input(part):
    with open("input.txt") as f:
        input_txt = f.read()

    grid_txt, moves_txt = input_txt.split("\n\n")
    if part == 2:
        grid_txt = grid_txt.replace("#", "##").replace(".", "..").replace("O", "[]").replace("@", "@.")

    grid = {c_idx + 1j*r_idx: c for r_idx, row in enumerate(grid_txt.splitlines())
                                for c_idx, c in enumerate(row) if c != "."}

    moves_map = {"^": -1j, "<": -1, "v": 1j, ">": 1}
    moves = [moves_map[m] for m in moves_txt.replace("\n", "")]

    return grid, moves


def print_map(grid, curr_pos, idx):
    grid_h, grid_w = max(int(p.imag) for p in grid) + 1, max(int(p.real) for p in grid) + 1
    grid_txt = "\n".join(["".join(["@" if c_idx + 1j*r_idx == curr_pos else grid.get(c_idx + 1j*r_idx, ".")
                                   for c_idx in range(grid_w)]) for r_idx in range(grid_h)])
    with open(f"out_{idx}.txt", "w") as f:
        f.write(grid_txt)


def solve_pt1(grid, moves):
    curr_pos, = [p for p in grid if grid[p] == "@"]
    del grid[curr_pos]

    for m in moves:
        idx = 1
        while True:
            next_object = grid.get(curr_pos + idx * m)
            if not next_object: # move curr pos and the first and last boxes
                if idx > 1:
                    del grid[curr_pos + 1 * m]
                    grid[curr_pos + idx * m] = "O"
                curr_pos += m
                break
            elif next_object == "#": # don't move
                break
            elif next_object == "O": # continue
                idx += 1

    score = sum(100*p.imag + p.real for p in grid if grid[p] == "O")

    return score


def solve(grid, moves):
    curr_pos, = [p for p in grid if grid[p] == "@"]
    del grid[curr_pos]

    for m_idx, m in enumerate(moves, 1):
        curr_positions = {curr_pos}
        movable_box_positions = set()
        blocked = False

        while curr_positions:
            next_p = curr_positions.pop() + m
            next_object = grid.get(next_p)
            if next_object == "#": # wall: don't move anything
                blocked = True
                break
            elif next_object in ("[", "]", "O"): # box: add positions to move
                new_positions = {next_p} | (set() if next_object == "O" else {next_p + 1 if next_object == "[" else next_p - 1})
                curr_positions.update(new_positions - movable_box_positions)
                movable_box_positions.update(new_positions - movable_box_positions)

        if not blocked: # not blocked: update all movable box positions
            grid_patch = {p + m: grid[p] for p in movable_box_positions}
            for del_pos in set(movable_box_positions) - set(grid_patch):
                del grid[del_pos]
            grid.update(grid_patch)
            curr_pos += m

    score = sum(100*p.imag + p.real for p in grid if grid[p] in ("[", "O"))

    return score


# PART 1
grid, moves = parse_input(part=1)
score = solve(grid, moves)
print(f"Part 1 solution: {score}")


# PART 2
grid, moves = parse_input(part=2)
score = solve(grid, moves)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass