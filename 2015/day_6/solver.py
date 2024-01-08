
import numpy as np


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    instructions = []
    for instr_txt in input_txt.splitlines():
        cmd, coords1_txt, _, coords2_txt = instr_txt.rsplit(maxsplit=3)
        cx1, cy1 = map(int, coords1_txt.split(","))
        cx2, cy2 = map(int, coords2_txt.split(","))
        instructions.append((cmd, (min(cx1, cx2), min(cy1, cy2)), (max(cx1, cx2), max(cy1, cy2))))
    return instructions


instructions = parse_input()

# part 1
grid = np.full((1000, 1000), False)
for cmd, (min_x, min_y), (max_x, max_y) in instructions:
    if cmd == "turn on":
        grid[min_x:max_x+1, min_y:max_y+1] = True
    elif cmd == "turn off":
        grid[min_x:max_x+1, min_y:max_y+1] = False
    elif cmd == "toggle":
        grid[min_x:max_x+1, min_y:max_y+1] = ~grid[min_x:max_x+1, min_y:max_y+1]
print("Part 1:", grid.sum())


# part 2
grid = np.full((1000, 1000), 0)
for cmd, (min_x, min_y), (max_x, max_y) in instructions:
    if cmd == "turn on":
        grid[min_x:max_x+1, min_y:max_y+1] += 1
    elif cmd == "turn off":
        grid[min_x:max_x+1, min_y:max_y+1] -= 1
        grid = np.clip(grid, a_min=0, a_max=np.inf)
    elif cmd == "toggle":
        grid[min_x:max_x+1, min_y:max_y+1] += 2
print("Part 2:", grid.sum())

if __name__ == "__main__":
    pass
