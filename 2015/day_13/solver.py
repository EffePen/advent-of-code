

def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()

    nodes = set()
    edges = dict()
    for edge_txt in input_txt.splitlines():
        edge_txt = edge_txt.replace("gain ", "").replace("lose ", "-").replace("would ", "").replace("happiness units by sitting next to ", "").replace(".", "")
        n1, dist_txt, n2 = edge_txt.split()
        dist = int(dist_txt)
        if n1 not in edges:
            edges[n1] = dict()
        edges[n1][n2] = dist
        nodes.update([n1, n2])
    return nodes, edges


def traverse(path, nodes, edges, final_distances):
    # if not all nodes has been visited, proceed
    if set(nodes) - set(path):
        last_node = path[-1]
        for next_node in set(edges.get(last_node, dict())) - set(path):
            traverse(path + [next_node], nodes, edges, final_distances)
    else:
        path.append(path[0]) # close the circle
        distance = sum(edges[path[idx]][path[idx+1]] + edges[path[idx+1]][path[idx]] for idx in range(len(path) - 1))
        final_distances.append(distance)

# part 1
nodes, edges = parse_input()
starting_nodes = list(edges.keys())
final_distances = []

for starting_node in starting_nodes:
    traverse([starting_node], nodes, edges, final_distances)

print("Part 1:", max(final_distances))

# part 2
myself_node_id = "Myself"
edges[myself_node_id] = dict()
for node in nodes:
    edges[myself_node_id][node] = 0
    edges[node][myself_node_id] = 0
nodes.add(myself_node_id)
starting_nodes = list(edges.keys())
final_distances = []

for starting_node in starting_nodes:
    traverse([starting_node], nodes, edges, final_distances)

print("Part 2:", max(final_distances))



if __name__ == "__main__":
    pass
