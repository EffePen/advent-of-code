

import numpy as np


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    return input_txt


pt1_cache = {}


def evolve_stone_v1(stone):
    if stone == 0:
        # the stone counter does not change, let the stone evolve
        stone = 1
        return [stone]
    else:
        # split the stone, evolve the 2 separately starting from 0 and for the time delta
        # get the delta in stones for both and add the initial counter
        stone_txt = str(stone)
        if len(stone_txt) % 2 == 0:
            l_stone = int(stone_txt[:len(stone_txt) // 2])
            r_stone = int(stone_txt[len(stone_txt) // 2:])
            return [l_stone, r_stone]
        else:
            # the stone counter does not change, let the stone evolve
            stone *= 2024
            return [stone]


def solve_pt1(input_txt, num_steps):
    stones = [int(e) for e in input_txt.split()]

    for step in range(num_steps):
        new_stones = []
        for stone in stones:
            delta = evolve_stone_v1(stone)
            new_stones += delta
        stones = new_stones

    score = len(stones)
    return score


def solve_pt2(input_txt, num_steps):
    # get graph edges for the evolution of 0
    toy_stones = [0]
    seen_nodes = set(toy_stones)
    neighbors = {}
    while True:
        new_stones = []
        for stone in toy_stones:
            if stone not in neighbors:
                neighbors[stone] = evolve_stone_v1(stone)
            new_stones += neighbors[stone]
        if len(set(new_stones) - seen_nodes) == 0:
            # if the same nodes start repeating, stop: the graph has been completely mapped
            break
        seen_nodes.update(new_stones)
        toy_stones = new_stones

    # define the adjacency matrix, and pre-calculate its powers from 1 to num_nodes
    # (M**n)_ij represents the number of paths that reach node "j" in n steps starting from node "i"
    # in this case, the number of stones "j" generated after n steps starting from node "i"
    n_nodes = len(neighbors)
    node2idx = {node: n_idx for n_idx, node in enumerate(sorted(neighbors))}
    idx2node = {n_idx: node for node, n_idx in node2idx.items()}
    adj_matrices = {}
    adj_matrices[0] = np.zeros(shape=(n_nodes, n_nodes), dtype=np.int64)
    for src, destinations in neighbors.items():
        for dst in destinations:
            adj_matrices[0][node2idx[src], node2idx[dst]] += 1
    # calculate matrix powers
    for step in range(1, num_steps+1):
        adj_matrices[step] = np.matmul(adj_matrices[step-1], adj_matrices[0])

    # evolve
    score = 0
    stones = [int(e) for e in input_txt.split()]
    for step in range(1, num_steps+1):
        new_stones = []
        for stone in stones:
            if stone in node2idx:
                # if the stone is one of the graph, get the final number of stones analytically from adj matrix powers
                idx = node2idx[stone]
                remaining_steps = num_steps - step
                final_num_nodes = sum(adj_matrices[remaining_steps][idx, :])
                score += final_num_nodes
            else:
                delta = evolve_stone_v1(stone)
                new_stones += delta
        stones = new_stones

    score += len(stones)
    return score


# PARSE INPUT
input_txt = parse_input()

# PART 1
score = solve_pt1(input_txt, num_steps=25)
print(f"Part 1 solution: {score}")


# PART 2
score = solve_pt2(input_txt, num_steps=75)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass
