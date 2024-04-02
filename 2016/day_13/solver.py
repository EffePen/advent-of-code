import re


input_num = 1362


def is_pos_open(pos):
    x, y = pos
    if x < 0 or y < 0:
        return False
    else:
        num = x * x + 3 * x + 2 * x * y + y + y * y + input_num
        bit_count = bin(num).count("1")
        if bit_count % 2 == 0:
            return True
        else:
            return False


arr = []
for x in range(20):
    arr.append([])
    for y in range(20):
        pos = (x, y)
        arr[-1].append("." if is_pos_open(pos) else "#")


lab_map = "\n".join(["".join(e) for e in arr])


def get_pos_neighbors(pos):
    neighbors = []
    for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        x, y = pos
        new_pos = (x + dx, y + dy)
        if is_pos_open(new_pos):
            neighbors.append(new_pos)
    return neighbors


# PART 1
spt_set = set()
distances = dict()
initial_pos = (1, 1)
distances[initial_pos] = 0

final_pos = (31, 39)
final_pos_reached = False
min_dist = 0
while not final_pos_reached or min_dist < 50:
    min_dist = min({d for p, d in distances.items() if p not in spt_set})
    min_dist_positions = {p for p, d in distances.items() if d == min_dist}
    candidate_positions = min_dist_positions - spt_set

    for pos in candidate_positions:
        spt_set.add(pos)
        pos_neighbors = set(get_pos_neighbors(pos)) - spt_set
        for n_pos in pos_neighbors:
            distances[n_pos] = min_dist + 1

            if n_pos == final_pos:
                final_pos_reached = True
                break

print(f"Part 1 solution: {distances[final_pos]}")
print(f"Part 2 solution: {len({p for p, d in distances.items() if d <= 50})}")

if __name__ == "__main__":
    pass