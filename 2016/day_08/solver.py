import itertools
import re

def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    instructions = input_txt.splitlines()
    return instructions


# PART 1
n_rows = 6
n_cols = 50

grid = [[False for _ in range(n_cols)] for _ in range(n_rows)]

instructions = parse_input()
for instr in instructions:
    if instr.startswith("rect"):
        shape = instr.split()[-1]
        width, height = [int(e) for e in shape.split("x")]
        for r_idx in range(height):
            for c_idx in range(width):
                grid[r_idx][c_idx] = True
    elif instr.startswith("rotate"):
        if "column" in instr:
            c_idx, shift = map(int, instr.split("x=")[1].split(" by "))
            v_shift = shift % n_rows
            t_grid = list(map(list, zip(*grid)))
            t_grid[c_idx] = t_grid[c_idx][-v_shift:] + t_grid[c_idx][:-v_shift]
            grid = list(map(list, zip(*t_grid)))
        elif "row" in instr:
            r_idx, shift = map(int, instr.split("y=")[1].split(" by "))
            r_shift = shift % n_cols
            grid[r_idx] = grid[r_idx][-r_shift:] + grid[r_idx][:-r_shift]
        else:
            raise ValueError
    else:
        raise ValueError


print(f"Part 1 solution: {sum([sum(row) for row in grid])}")
print(f"Part 2 solution:")
print("\n".join(["".join(["#" if e else "." for e in row]) for row in grid]))

if __name__ == "__main__":
    pass