
import os
import ast
import math


def parse_input():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")) as f:
        input_txt = f.read()
    coords = [ast.literal_eval(f"({l})") for l in input_txt.splitlines()]
    return coords


def euclidean_dist(c1, c2):
    return sum((x1 - x2)**2 for x1, x2 in zip(c1, c2))**1/2


def connect(c1, c2, conn_components):
    c1_conn_comp = [(cc_idx, cc) for cc_idx, cc in enumerate(conn_components) if c1 in cc]
    c2_conn_comp = [(cc_idx, cc) for cc_idx, cc in enumerate(conn_components) if c2 in cc]
    if not c1_conn_comp and not c2_conn_comp:
        # crete a new connected component
        conn_components.append({c1, c2})
    elif c1_conn_comp and not c2_conn_comp:
        # add element 2 to already existing connected component
        c1_conn_comp[0][1].add(c2)
    elif c2_conn_comp and not c1_conn_comp:
        # add element 1 to already existing connected component
        c2_conn_comp[0][1].add(c1)
    elif c1_conn_comp[0][0] == c2_conn_comp[0][0]:
        # already in the same connected component, skip
        pass
    else:
        # merge connected components
        conn_components[min(c1_conn_comp[0][0], c2_conn_comp[0][0])].update(conn_components[max(c1_conn_comp[0][0], c2_conn_comp[0][0])])
        del conn_components[max(c1_conn_comp[0][0], c2_conn_comp[0][0])]
    return conn_components


def solve_pt1(coords, limit=1000):
    conn_components = []
    distances = []
    for c1_idx, c1 in enumerate(coords):
        for c2 in coords[c1_idx + 1:]:
            distances.append((euclidean_dist(c1, c2), (c1, c2)))
    
    distances = sorted(distances)
    for _, (c1, c2) in distances[:limit]:
        conn_components = connect(c1, c2, conn_components)
    
    conn_components = sorted(conn_components, key=lambda x: len(x), reverse=True)
    score = math.prod(len(x) for x in conn_components[:3])
    return score


def solve_pt2(coords):
    conn_components = []
    distances = []
    for c1_idx, c1 in enumerate(coords):
        for c2 in coords[c1_idx + 1:]:
            distances.append((euclidean_dist(c1, c2), (c1, c2)))
    
    distances = sorted(distances)
    for _, (c1, c2) in distances:
        conn_components = connect(c1, c2, conn_components)
        if len(conn_components) == 1 and len(conn_components[0]) == len(coords):
            score = c1[0] * c2[0]
            return score



# PARSE INPUT
coords = parse_input()

# PART 1
score = solve_pt1(coords, limit=1000)
print(f"Part 1 solution: {score}")

# PART 2
score = solve_pt2(coords)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass