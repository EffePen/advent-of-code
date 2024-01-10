

def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()

    nodes = set()
    edges = dict()
    for edge_txt in input_txt.splitlines():
        edge_nodes_txt, dist_txt = edge_txt.split(" = ")
        dist = int(dist_txt)
        n1, n2 = edge_nodes_txt.split(" to ")
        if n1 not in edges:
            edges[n1] = dict()
        edges[n1][n2] = dist
        if n2 not in edges:
            edges[n2] = dict()
        edges[n2][n1] = dist
        nodes.update([n1, n2])
    return nodes, edges


def traverse(path, nodes, edges, final_distances):
    # if not all nodes has been visited, proceed
    if set(nodes) - set(path):
        last_node = path[-1]
        for next_node in set(edges.get(last_node, dict())) - set(path):
            traverse(path + [next_node], nodes, edges, final_distances)
    else:
        distance = sum(edges[path[idx]][path[idx+1]] for idx in range(len(path) - 1))
        final_distances.append(distance)

# part 1 & 2
nodes, edges = parse_input()
starting_nodes = list(edges.keys())
final_distances = []

for starting_node in starting_nodes:
    traverse([starting_node], nodes, edges, final_distances)

print("Part 1:", min(final_distances))
print("Part 2:", max(final_distances))


if __name__ == "__main__":
    pass
