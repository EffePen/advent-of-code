
import sys
from collections import defaultdict


with open("a_input.txt") as f:
    input_txt = f.read()

rows = [[int(c) for c in r] for r in input_txt.splitlines()]
cols = [list(l) for l in zip(*rows)]
n_rows = len(rows)
n_cols = len(rows[0])

start_node = (0, 0)
end_node = (n_rows-1, n_cols-1)

v_spt_set = set()
h_spt_set = set()

h_distances = defaultdict(lambda: sys.maxsize)
v_distances = defaultdict(lambda: sys.maxsize)

h_distances[start_node] = v_distances[start_node] = 0

while (end_node not in v_spt_set) and (end_node not in h_spt_set):
    min_v_distance = min(v for k, v in v_distances.items() if k not in v_spt_set)
    min_h_distance = min(v for k, v in h_distances.items() if k not in h_spt_set)

    # if the min distance is the one obtained by a last "horizontal" move (=> in h distance),
    # search vertical neighbours and update vertical distances
    if min_h_distance <= min_v_distance:
        starting_nodes = [node for node, dist in h_distances.items() if dist == min_h_distance]
        for s_node in starting_nodes:
            h_spt_set.add(s_node)
            r_idx, c_idx = s_node
            deltas = [delta for delta in [-10, -9, -8, -7, -6, -5, -4, 4, 5, 6, 7, 8, 9, 10] if 0 <= r_idx + delta < n_rows]
            for delta in deltas:
                e_node = (r_idx + delta, c_idx)
                if delta > 0:
                    dist_delta = sum(cols[c_idx][r_idx+1: r_idx+delta+1])
                else:
                    dist_delta = sum(cols[c_idx][r_idx+delta: r_idx])

                if v_distances[e_node] > min_h_distance + dist_delta:
                    v_distances[e_node] = min_h_distance + dist_delta

    # if the min distance is the one obtained by a last "vertical" move (=> in v distance),
    # search horizontal neighbours and update horizontal distances
    if min_v_distance <= min_h_distance:
        starting_nodes = [node for node, dist in v_distances.items() if dist == min_v_distance]
        for s_node in starting_nodes:
            v_spt_set.add(s_node)
            r_idx, c_idx = s_node
            deltas = [delta for delta in [-10, -9, -8, -7, -6, -5, -4, 4, 5, 6, 7, 8, 9, 10] if 0 <= c_idx + delta < n_cols]
            for delta in deltas:
                e_node = (r_idx, c_idx + delta)
                if delta > 0:
                    dist_delta = sum(rows[r_idx][c_idx+1: c_idx+delta+1])
                else:
                    dist_delta = sum(rows[r_idx][c_idx+delta: c_idx])

                if h_distances[e_node] > min_v_distance + dist_delta:
                    h_distances[e_node] = min_v_distance + dist_delta


# p1
min_distance_start2end = min(v_distances[end_node], h_distances[end_node])
print(min_distance_start2end)


if __name__ == "__main__":
    pass