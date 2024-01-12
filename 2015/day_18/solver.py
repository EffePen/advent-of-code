
import numpy as np
import scipy


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    input_txt_adj = input_txt.replace("#", "1").replace(".", "0").splitlines()
    grid = np.array([list(map(int, line_txt)) for line_txt in input_txt_adj])
    return grid


def part1(grid):
    # create mask for neighbors only
    neigh_mask = np.full((3, 3), 1)
    neigh_mask[1,1] = 0
    n_iter = 100
    for idx in range(n_iter):
        neigh_cnt = scipy.signal.convolve2d(grid, neigh_mask, mode='same', boundary='fill', fillvalue=0)
        off2on = ~grid & (neigh_cnt == 3)
        on2on = grid & ((neigh_cnt == 2) | (neigh_cnt == 3))
        grid = off2on | on2on

    return grid.sum()


def part2(grid):
    # create mask for neighbors only
    neigh_mask = np.full((3, 3), 1)
    neigh_mask[1,1] = 0
    n_iter = 100
    n_rows, n_cols = grid.shape
    grid[0,0] = grid[0,n_cols-1] = grid[n_rows-1,0] = grid[n_rows-1,n_cols-1] = 1
    for idx in range(n_iter):
        neigh_cnt = scipy.signal.convolve2d(grid, neigh_mask, mode='same', boundary='fill', fillvalue=0)
        off2on = ~grid & (neigh_cnt == 3)
        on2on = grid & ((neigh_cnt == 2) | (neigh_cnt == 3))
        grid = off2on | on2on
        grid[0, 0] = grid[0, n_cols - 1] = grid[n_rows - 1, 0] = grid[n_rows - 1, n_cols - 1] = 1

    return grid.sum()


# input
grid = parse_input()

# part 1
num_on = part1(grid)
print("Part 1:", num_on)

# part 2
num_on = part2(grid)
print("Part 2:", num_on)


if __name__ == "__main__":
    pass
