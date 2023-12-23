import functools
import os
import sys
import time
from collections import defaultdict


def parse_file():
    with open("a_input.txt") as f:
        input_txt = f.read()

    map = input_txt.splitlines()
    return map


@functools.lru_cache(maxsize=None)
def get_next_moves(slice, relative_pos):
    tot_possible_moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    # get only possible ones
    possible_moves = set()
    r_idx, c_idx = relative_pos
    for mv in tot_possible_moves:
        dr, dc = mv
        nr_idx = r_idx + dr
        nc_idx = c_idx + dc
        try:
            nblock = slice[nr_idx][nc_idx]
        except IndexError:
            continue

        if nblock == "." or nblock in ("<", ">", "v", "^"):
            possible_moves.add(mv)
        elif nblock == "#":
            continue
        else:
            raise ValueError
    return possible_moves


map = parse_file()
n_rows = len(map)
n_cols = len(map[0])
start_pos = (0, map[0].index("."))
end_pos = (n_rows-1, map[-1].index("."))
first_move = [1, 0]
curr_pos = (start_pos[0] + first_move[0], start_pos[1] + first_move[1])

nodes = {start_pos}
edges = {}
curr_edge = [start_pos, curr_pos]
curr_positions_prev_moves = [(curr_edge, first_move)]


# parse graph
while curr_positions_prev_moves:
    next_positions_curr_moves = []
    for curr_edge, prev_move in curr_positions_prev_moves:
        # get possible next moves (and remove last reversed one, if present)
        curr_pos = curr_edge[-1]
        r_idx, c_idx = curr_pos
        rs_idx = max(r_idx - 1, 0)
        re_idx = min(r_idx + 2, n_rows-1)
        cs_idx = max(c_idx - 1, 0)
        ce_idx = min(c_idx + 2, n_cols-1)
        relative_pos = (r_idx - rs_idx, c_idx - cs_idx)
        slice = tuple(r[cs_idx:ce_idx] for r in map[rs_idx:re_idx])
        next_moves = get_next_moves(slice, relative_pos) - {(- prev_move[0], - prev_move[1])}

        # if trail forks, add node, terminate edge and start new ones
        start_new_edge = len(next_moves) > 1 or curr_pos == end_pos
        if start_new_edge:
            # sort start and end positions of the edge and save the edge
            edge_start_pos, edge_end_pos = curr_edge[0], curr_edge[-1]
            edge_id = tuple(sorted([edge_start_pos, edge_end_pos], key=lambda x: x))

            # if new edge, or more than one edge connecting 2 nodes, keep the longest
            if (edge_id not in edges) or (len(curr_edge) > len(edges[edge_id])):
                edges[edge_id] = curr_edge

            # if the "new" node has been already visited, stop (its edges have already been explored)
            if curr_pos in nodes:
                continue

            # add curr pos to nodes
            nodes.add(curr_pos)

        # evolve position
        for mv_idx, mv in enumerate(next_moves):
            next_pos = (curr_pos[0] + mv[0], curr_pos[1] + mv[1])
            if start_new_edge:
                # if new ones, duplicate fork edges
                updated_edge = [curr_pos, next_pos]
            else:
                curr_edge.append(next_pos)
                updated_edge = curr_edge

            next_positions_curr_moves.append((updated_edge, mv))
    curr_positions_prev_moves = next_positions_curr_moves

# dijkstra (the edges are weighted by negative trail len excluding final node => -1)
start_node = start_pos
end_node = end_pos
edges_weight = {eid: - (len(edge) - 1) for eid, edge in edges.items()}
spt_set = set()
distances = defaultdict(lambda: sys.maxsize)
distances[start_node] = 0

while end_node not in spt_set:
    min_distance = min(distances.values())
    starting_nodes = [npos for npos, dist in distances.items()
                      if dist == min_distance if npos not in spt_set]

    for node in starting_nodes:
        # edd node to explored one
        spt_set.add(node)

        # search neighbors and update dist
        for (n1, n2), weight in edges_weight.items():
            if node in (n1, n2):
                new_node = n1 if node == n2 else n2
                if new_node not in spt_set:
                    distances[new_node] = distances[node] + weight


if __name__ == "__main__":
    pass
