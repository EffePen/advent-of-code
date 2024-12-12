
from collections import defaultdict


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    return input_txt


def solve_pt1(input_txt):
    grid = {}
    for r_idx, row in enumerate(input_txt.splitlines()):
        for c_idx, c in enumerate(row):
            grid[c_idx + r_idx * 1j] = c

    seen_positions = set()
    areas = defaultdict(int)
    perimeters = defaultdict(int)

    total_positions = set(grid.keys())
    next_positions = list(total_positions - seen_positions)[0:1]
    group_idx = 0

    while total_positions - seen_positions:
        candidate_next_positions = []
        for curr_pos in next_positions:
            areas[group_idx] += 1
            seen_positions.add(curr_pos)

            # check if neighbors are of the same type
            for delta in [1, -1, 1j, -1j]:
                cnp = curr_pos + delta

                if grid.get(cnp) == grid[curr_pos]: # same plant type => add position for further exploration
                    candidate_next_positions.append(cnp)
                else: # different plant type => increase perimeter
                    perimeters[group_idx] += 1

        candidate_next_positions = set(candidate_next_positions) - seen_positions
        if not candidate_next_positions:
            next_positions = list(total_positions - seen_positions)[0:1]
            group_idx += 1
        else:
            next_positions = candidate_next_positions

    score = 0
    for group_idx in areas.keys():
        score += areas[group_idx] * perimeters[group_idx]

    return score


def solve_pt2(input_txt):
    grid = {}
    for r_idx, row in enumerate(input_txt.splitlines()):
        for c_idx, c in enumerate(row):
            grid[c_idx + r_idx * 1j] = c

    seen_positions = set()
    areas = defaultdict(int)
    perimeters = defaultdict(list)

    total_positions = set(grid.keys())
    next_positions = list(total_positions - seen_positions)[0:1]
    group_idx = 0

    while total_positions - seen_positions:
        candidate_next_positions = []
        for curr_pos in next_positions:
            areas[(group_idx, grid[curr_pos])] += 1
            seen_positions.add(curr_pos)

            # check if neighbors are of the same type
            for delta in [1, -1, 1j, -1j]:
                cnp = curr_pos + delta

                if grid.get(cnp) == grid[curr_pos]: # same plant type => add position for further exploration
                    candidate_next_positions.append(cnp)
                else: # different plant type => save position and clockwise direction of the perimeter
                    perimeters[(group_idx, grid[curr_pos])].append((cnp, delta * 1j))

        candidate_next_positions = set(candidate_next_positions) - seen_positions
        if not candidate_next_positions:
            next_positions = list(total_positions - seen_positions)[0:1]
            group_idx += 1
        else:
            next_positions = candidate_next_positions

    score = 0
    for group_idx, plant_type in areas.keys():
        # count straight lines in perimeter
        tot_p_pos = set(perimeters[(group_idx, plant_type)])
        seen_p_positions = set()

        # get first perimeter positions
        next_p_positions = list(set(perimeters[(group_idx, plant_type)]) - seen_p_positions)[0:1]
        seen_p_positions.update(next_p_positions)
        line_idx = 0
        lines = defaultdict(list)
        lines[line_idx] += next_p_positions

        while tot_p_pos - seen_p_positions:
            candidate_next_p_positions = set()
            for p_pos, side_direction in next_p_positions:
                next_p_pos_ahead = p_pos + side_direction
                next_p_pos_behind = p_pos - side_direction

                # get new perimeter positions in line, among those that have not been seen yet
                if (next_p_pos_ahead, side_direction) in perimeters[(group_idx, plant_type)]:
                    candidate_next_p_positions.add((next_p_pos_ahead, side_direction))
                if (next_p_pos_behind, side_direction) in perimeters[(group_idx, plant_type)]:
                    candidate_next_p_positions.add((next_p_pos_behind, side_direction))
                candidate_next_p_positions = candidate_next_p_positions - seen_p_positions

            if candidate_next_p_positions: # further positions along the line
                next_p_positions = candidate_next_p_positions
                lines[line_idx] += next_p_positions
            elif tot_p_pos - seen_p_positions: # no further positions along the line
                # start a new line
                next_p_positions = list(set(perimeters[(group_idx, plant_type)]) - seen_p_positions)[0:1]
                line_idx += 1
                lines[line_idx] += next_p_positions

            seen_p_positions.update(next_p_positions)

        area = areas[(group_idx, plant_type)]
        num_lines = len(lines)
        price = area * num_lines
        score += price

    return score


# PARSE INPUT
input_txt = parse_input()

# PART 1
score = solve_pt1(input_txt)
print(f"Part 1 solution: {score}")


# PART 2
score = solve_pt2(input_txt)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass