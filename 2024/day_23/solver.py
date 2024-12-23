

from collections import defaultdict


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    edges = [e.split("-") for e in input_txt.splitlines()]
    return edges


def solve(edges, part):
    # part 1
    nodes = set()
    for edge in edges:
        nodes.update(edge)

    node_neighbors = defaultdict(set)
    for n1, n2 in edges:
        node_neighbors[n1].add(n2)
        node_neighbors[n2].add(n1)

    starting_nodes = {n for n in nodes if n.startswith("t")}
    node_sets = set()
    for n1 in starting_nodes:
        if len(node_neighbors[n1]) < 2:
            continue

        for n2 in node_neighbors[n1]:
            for n3 in node_neighbors[n1]:
                if n2 in node_neighbors[n3] and n3 in node_neighbors[n2]:
                    node_sets.add(tuple(sorted([n1, n2, n3])))
    if part == 1:
        return len(node_sets)

    # part 2
    candidate_node_sets = node_sets
    while len(candidate_node_sets) > 1:
        new_candidate_node_sets = set()
        for ns in candidate_node_sets:
            for n, neighbors in node_neighbors.items():
                if set(ns) <= neighbors:
                    new_candidate_node_sets.add(tuple(sorted(ns + (n,))))
        candidate_node_sets = new_candidate_node_sets

    return ",".join(candidate_node_sets.pop())


# PARSE INPUT
edges = parse_input()

# PART 1
score = solve(edges, part=1)
print(f"Part 1 solution: {score}")


# PART 2
score = solve(edges, part=2)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass