

def parse_input():
    with open("input.txt") as f:
        code = [int(e) for e in f.read().split()]
    return code


def store_node_info(code, start_idx, nodes_dict):
    num_child_nodes = code[start_idx]
    num_metadata = code[start_idx+1]

    # Iterate recursively over children nodes, so that their info is filled before moving forward
    children_idxs = []
    end_idx = start_idx + 2
    for idx in range(num_child_nodes):
        children_idxs.append(end_idx)
        end_idx = store_node_info(code, end_idx, nodes_dict)

    metadata = code[end_idx:end_idx+num_metadata]

    if num_child_nodes == 0:
        # If it has no children nodes, get score from its metadata entries
        score = sum(metadata)
    else:
        # If it has children nodes, calculate score starting from their scores
        # (this is assured by the previous iteration)
        children_refs = [r for r in metadata if 0 < r <= num_child_nodes]
        score = sum([nodes_dict[children_idxs[r-1]][2] for r in children_refs])

    # Store the node info
    nodes_dict[start_idx] = (children_idxs, metadata, score)
    return end_idx+num_metadata


def solve_pt12(code):
    nodes_dict = {}
    _ = store_node_info(code, start_idx=0, nodes_dict=nodes_dict)

    score_pt1 = 0
    for n_idx, (_, metadata, _) in nodes_dict.items():
        score_pt1 += sum(metadata)

    score_pt2 = nodes_dict[0][2]

    return score_pt1, score_pt2


code = parse_input()

# ######## PART 1 & 2
score_pt1, score_pt2 = solve_pt12(code)
print("Part 1 solution: ", score_pt1)
print("Part 2 solution: ", score_pt2)


if __name__ == "__main__":
    pass