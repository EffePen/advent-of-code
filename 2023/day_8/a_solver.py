
import re

with open("a_input.txt") as f:
    input_txt = f.read()

rl_map = {"L": 0, "R": 1}
path, graph_adj = [e.strip() for e in input_txt.split("\n\n")]
path_list = [rl_map[i] for i in path]
graph_adj_tuples = [e.split() for e in re.sub(r"[^A-Z\s]", "", graph_adj).split("\n")]
graph_adj_dict = {e[0]: e[1:] for e in graph_adj_tuples}

idx = 0
next_node = ""
curr_node = "AAA"
while curr_node != "ZZZ":
    path_list_idx = idx % len(path_list)
    lr_idx = path_list[path_list_idx]
    curr_node = graph_adj_dict[curr_node][lr_idx]
    idx += 1

print(idx)

if __name__ == "__main__":
    pass
