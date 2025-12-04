
import numpy as np


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read().replace("@", "1").replace(".", "0")
    diagram = np.array([[int(e) for e in l] for l in input_txt.splitlines()], int)
    return diagram


def solve_pt1(diagram):
    score = 0
    h, w = diagram.shape
    for v_idx in range(h):
        for h_idx in range(w):
            if not diagram[v_idx, h_idx]:
                continue
            sub_diagram = diagram[max(v_idx-1, 0):min(v_idx+2, h), max(h_idx-1, 0):min(h_idx+2, w)]
            n_rolls = sub_diagram.sum() - 1
            if diagram[v_idx, h_idx] and n_rolls < 4:
                score += 1
    return score


def solve_pt2(diagram):
    score = 0
    h, w = diagram.shape

    while True:
        coords = []
        for v_idx in range(h):
            for h_idx in range(w):
                if not diagram[v_idx, h_idx]:
                    continue
                sub_diagram = diagram[max(v_idx-1, 0):min(v_idx+2, h), max(h_idx-1, 0):min(h_idx+2, w)]
                n_rolls = sub_diagram.sum() - 1
                if n_rolls < 4:
                    coords.append((v_idx, h_idx))
        if coords:
            score += len(coords)
            for v_idx, h_idx in coords:
                diagram[v_idx, h_idx] = 0
        else:
            break
    return score


def solve_pt2_v2(diagram):
    score = 0
    h, w = diagram.shape

    while True:
        prev_score = score
        for v_idx in range(h):
            for h_idx in range(w):
                if not diagram[v_idx, h_idx]:
                    continue
                sub_diagram = diagram[max(v_idx-1, 0):min(v_idx+2, h), max(h_idx-1, 0):min(h_idx+2, w)]
                n_rolls = sub_diagram.sum() - 1
                if n_rolls < 4:
                    score += 1
                    diagram[v_idx, h_idx] = 0

        if score == prev_score:
            break
    return score


# PARSE INPUT
diagram = parse_input()

# PART 1
score = solve_pt1(diagram)
print(f"Part 1 solution: {score}")


# PART 2
score = solve_pt2_v2(diagram)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass