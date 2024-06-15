

def parse_input():
    with open("input.txt") as f:
        input_lines = f.read().splitlines()

    linked_nodes = dict()
    for l in input_lines:
        node, linked_nodes_str = l.split(" <-> ")
        linked_nodes[node] = linked_nodes_str.split(", ")
    return linked_nodes


def get_all_subgraph_nodes(linked_nodes, starting_node):
    subgraph_nodes = {starting_node}
    next_nodes = [starting_node]
    while next_nodes:
        next_node_candidates = []
        for node in next_nodes:
            next_node_candidates += linked_nodes[node]
        next_nodes = set(next_node_candidates) - subgraph_nodes
        subgraph_nodes.update(next_nodes)
    return subgraph_nodes


def get_all_groups(linked_nodes):
    nodes_not_in_group = set(linked_nodes)
    groups = []
    while nodes_not_in_group:
        n = next(iter(nodes_not_in_group))
        group = get_all_subgraph_nodes(linked_nodes, starting_node=n)
        groups.append(group)
        nodes_not_in_group -= group
    return groups


linked_nodes = parse_input()


# ######## PART 1
subgraph_nodes = get_all_subgraph_nodes(linked_nodes, starting_node="0")
print("Part 1 solution: ", len(subgraph_nodes))

# ######## PART 2
groups = get_all_groups(linked_nodes)
print("Part 2 solution: ", len(groups))


if __name__ == "__main__":
    pass