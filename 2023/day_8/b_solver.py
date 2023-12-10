import itertools
import re
from functools import reduce

with open("a_input.txt") as f:
    input_txt = f.read()

rl_map = {"L": 0, "R": 1}
path, graph_adj = [e.strip() for e in input_txt.split("\n\n")]
path_list = [rl_map[i] for i in path]
graph_adj_tuples = [e.split() for e in re.sub(r"[^A-Z0-9\s]", "", graph_adj).split("\n")]
graph_adj_dict = {e[0]: e[1:] for e in graph_adj_tuples}

idx = 0
next_node = ""
curr_nodes = [n for n in graph_adj_dict if n.endswith("A")]
curr_z_nodes = []
z_nodes_indices = {n: [] for n in graph_adj_dict if n.endswith("Z")}

while not all([len(z_nodes_indices[d]) >= 2 for d in z_nodes_indices]):
    curr_z_nodes = [n for n in curr_nodes if n.endswith("Z")]
    for d in curr_z_nodes:
        z_nodes_indices[d].append(idx)

    path_list_idx = idx % len(path_list)
    lr_idx = path_list[path_list_idx]
    curr_nodes = [graph_adj_dict[curr_node][lr_idx] for curr_node in curr_nodes]
    idx += 1

# check periodicity and number of z nodes
assert all([z_nodes_indices[d][1] == 2*z_nodes_indices[d][0] for d in z_nodes_indices])
assert len(z_nodes_indices) == len(curr_nodes)

z_node_periodicity = [z_nodes_indices[d][0] for d in z_nodes_indices]


def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


z_node_pfactors = [factors(p) for p in z_node_periodicity]
z_node_pfactors_adj = []
for fs in z_node_pfactors:
    for f in fs:
        # if prime number or if not 1 or tot number
        if len(fs) == 2 or f not in (1, max(fs)):
            z_node_pfactors_adj.append(f)

score = 1
factors = set(z_node_pfactors_adj)
for p in factors:
    score *= p
print(score)

if __name__ == "__main__":
    pass
