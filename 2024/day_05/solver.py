

import re
from collections import defaultdict


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()

    dependencies_txt, updates_txt = input_txt.split("\n\n")

    # group each node dependencies
    dependencies = defaultdict(list)
    for r in dependencies_txt.splitlines():
        src, dst = [int(e) for e in r.split("|")]
        dependencies[dst].append(src)

    updates = [[int(e) for e in r.split(",")] for r in updates_txt.splitlines()]

    return dependencies, updates


def solve_pt1(dependencies, updates):
    score = 0

    for update_list in updates:
        # for each list element, check if it has dependencies among the following nodes
        seen_nodes = set()
        ordered = True
        for e in update_list:
            curr_dependencies = set(dependencies[e]) & set(update_list)
            if curr_dependencies - seen_nodes:
                ordered = False
                break
            seen_nodes.add(e)

        # if the list is completely ordered, add its central element to the total score
        if ordered:
            delta = update_list[(len(update_list) // 2)]
            score += delta

    return score


def solve_pt2(dependencies, updates):
    score = 0

    for update_list in updates:
        # for each list element, check if it has dependencies among the following nodes
        seen_nodes = set()
        ordered = True
        for e in update_list:
            curr_dependencies = set(dependencies[e]) & set(update_list)
            if curr_dependencies - seen_nodes:
                ordered = False
                break
            seen_nodes.add(e)

        # if it is not ordered, sort it first and then add its central element to the total score
        if not ordered:
            ordered_list = list()
            while set(update_list) - set(ordered_list):
                # get the only node without dependencies (breaks if more than one)
                next_node, = [e for e in set(update_list) - set(ordered_list)
                              if not set(dependencies[e]) & set(update_list) - set(ordered_list)]
                ordered_list.append(next_node)

            delta = ordered_list[(len(ordered_list) // 2)]
            score += delta

    return score


# PARSE INPUT
dependencies, updates = parse_input()

# PART 1
score = solve_pt1(dependencies, updates)
print(f"Part 1 solution: {score}")


# PART 2
score = solve_pt2(dependencies, updates)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass
