
import re
import collections


def parse_input():
    with open("input.txt") as f:
        input_lines = f.read().splitlines()

    nodes = dict()
    edges = []
    for input_line in input_lines:
        try:
            node_info, leaves = input_line.split(" -> ")
            leaves = leaves.split(", ")
        except ValueError:
            node_info = input_line
            leaves = []
        (node_name, node_size), = re.findall(r"([^\s]+) \((\d+)\)", node_info)
        nodes[node_name] = int(node_size)
        edges += [(node_name, leaf_name) for leaf_name in leaves]
    return nodes, edges


def find_root(nodes, edges):
    root_nodes = []
    for node in nodes:
        next_node = node
        while True:
            node_edges = [e for e in edges if next_node == e[1]]
            if node_edges:
                edge, = node_edges
                next_node = edge[0]
            else:
                root_nodes.append(next_node)
                break
    root_node, = set(root_nodes)
    return root_node


def balance_tower(nodes, edges):
    total_node_weight = nodes.copy()
    # for each node, descend the tower and add its weight to the lower ones
    for node, node_weight in nodes.items():
        next_node = node
        while True:
            node_bw_edges = [e for e in edges if next_node == e[1]]
            if node_bw_edges:
                edge, = node_bw_edges
                next_node = edge[0]
                total_node_weight[next_node] += node_weight
            else:
                break

    # check each node's subtowers weight
    for node in nodes:
        node_fw_edges = [e for e in edges if node == e[0]]
        if node_fw_edges:
            fw_nodes = [e[1] for e in node_fw_edges]
            fw_weights = [total_node_weight[n] for n in fw_nodes]
            if len(set(fw_weights)) > 1:
                (tot_right_weight, _), (tot_wrong_weight, _) = \
                    collections.Counter(fw_weights).most_common()
                delta = tot_right_weight - tot_wrong_weight
                wrong_node, = [n for n in fw_nodes if total_node_weight[n] == tot_wrong_weight]
                wrong_weight = nodes[wrong_node]
                right_weight = wrong_weight + delta
                return right_weight


nodes, edges = parse_input()

# ######## PART 1
root = find_root(nodes, edges)
print("Part 1 solution: ", root)


# ######## PART 2
right_weight = balance_tower(nodes, edges)
print("Part 2 solution: ", right_weight)


if __name__ == "__main__":
    pass