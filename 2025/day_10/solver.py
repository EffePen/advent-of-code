
import os
import ast
import math
import itertools


def parse_input():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")) as f:
        input_txt = f.read()
    
    machines = []
    for l in input_txt.splitlines():
        parts = l.split()
        indicator = int("".join(["1" if e == "#" else "0" for e in parts[0][1:-1]]), 2)
        joltage = ast.literal_eval(f"({parts[-1][1:-1]})")
        buttons = [int("".join(["1" if idx in ast.literal_eval(b[:-1] + ",)") else "0" for idx in range(len(parts[0][1:-1]))]), 2) 
                   for b in parts[1:-1]]
        machines.append((indicator, buttons, joltage))
    return machines


def solve_pt1(machines):
    score = 0
    for indicator, buttons, _ in machines:
        toggles = 0
        curr_states = [0]
        visited_states = set(curr_states)
        while indicator not in curr_states:
            prev_states = curr_states
            curr_states = set(s ^ b for s in prev_states for b in buttons) - visited_states
            toggles += 1
        score += toggles
    return score


def solve_pt2(machines):
    score = 0
    return score


# PARSE INPUT
machines = parse_input()

# PART 1
score = solve_pt1(machines)
print(f"Part 1 solution: {score}")

# PART 2
score = solve_pt2(machines)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass