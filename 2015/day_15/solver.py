
import numpy as np


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    ingredients = dict()
    for line_txt in input_txt.splitlines():
        ingr_id, vals_txt = line_txt.split(": ")
        ingredients[ingr_id] = [int(e.split()[1]) for e in vals_txt.split(", ")]
    return ingredients


def part12(ingredients):
    max_score = 0
    max_cal_score = 0
    # values matrix excluding the calories
    properties_matrix = np.array([vals for vals in ingredients.values()])

    assert len(ingredients) == 4
    for q1 in range(0, MAX_Q + 1):
        for q2 in range(0, MAX_Q + 1 - q1):
            for q3 in range(0, MAX_Q + 1 - q1 - q2):
                q4 = MAX_Q - q1 - q2 - q3
                q = np.array([q1, q2, q3, q4])
                tot_vals = np.dot(properties_matrix.T, q)
                score = np.prod(np.clip(tot_vals[:-1], a_min=0, a_max=None), initial=1)
                tot_cals = tot_vals[-1]
                if score > max_score:
                    max_score = score
                if tot_cals == TOT_CALS and score > max_cal_score:
                    max_cal_score = score

    return max_score, max_cal_score


MAX_Q = 100
TOT_CALS = 500

# input
ingredients = parse_input()

# part 1 & 2
max_score, max_cal_score = part12(ingredients)
print("Part 1:", max_score)
print("Part 2:", max_cal_score)

if __name__ == "__main__":
    pass
