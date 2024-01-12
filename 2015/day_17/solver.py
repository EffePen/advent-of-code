
import itertools
import numpy as np


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    sizes = [int(line_txt) for line_txt in input_txt.splitlines()]
    return sizes


def part1(sizes):
    num_ok = 0
    n_bits = len(sizes)
    batch_bit_size = 19
    batch_truth_table = np.array(list(itertools.product([False, True], repeat=batch_bit_size)))
    iter_truth_table = np.array(list(itertools.product([False, True], repeat=n_bits - batch_bit_size)))

    n_rows, _ = iter_truth_table.shape
    for r_idx in range(n_rows):
        sizes_batch = sizes[:batch_bit_size]
        sizes_iter = sizes[batch_bit_size:]

        tot_sizes = np.dot(batch_truth_table, sizes_batch) + np.dot(iter_truth_table[r_idx,:], sizes_iter)
        num_ok += (tot_sizes == TOT_SIZE).sum()

    return num_ok


def part2(sizes):
    n_bits = len(sizes)
    batch_truth_table = np.array(list(itertools.product([False, True], repeat=n_bits)))

    tot_sizes = np.dot(batch_truth_table, sizes)
    tot_sizes_ok = (tot_sizes == TOT_SIZE)
    num_containers = batch_truth_table.sum(axis=1)
    min_num_containers = num_containers[tot_sizes_ok].min()
    num_containers_ok = (num_containers == min_num_containers)
    num_ok = (num_containers_ok & tot_sizes_ok).sum()

    return num_ok


TOT_SIZE = 150


# input
sizes = parse_input()

# part 1
num_ok = part1(sizes)
print("Part 1:", num_ok)

# part 2
num_ok = part2(sizes)
print("Part 2:", num_ok)


if __name__ == "__main__":
    pass
