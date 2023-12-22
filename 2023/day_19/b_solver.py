
import copy

with open("a_input.txt") as f:
    input_txt = f.read()


instructions_str, products_str = input_txt.split("\n\n")

instructions_dict = {}
for instruction_str in instructions_str.splitlines():
    node_list = []
    values_intervals = {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}
    instr_id, instruction_str = instruction_str.split("{")

    for instruction in instruction_str.strip("}").split(","):
        # if split, get condition for that destination
        if ":" in instruction:
            cond_str, dst_id = instruction.split(":")
            cond_variable = cond_str[0]
            cond_op = cond_str[1]
            cond_value = int(cond_str[2:])

            yes_values = copy.deepcopy(values_intervals)
            if cond_op == "<":
                yes_values[cond_variable] = [yes_values[cond_variable][0], cond_value - 1]
                values_intervals[cond_variable] = [cond_value, values_intervals[cond_variable][1]]
            elif cond_op == ">":
                yes_values[cond_variable] = [cond_value + 1, yes_values[cond_variable][1]]
                values_intervals[cond_variable] = [values_intervals[cond_variable][0], cond_value]
            else:
                raise RuntimeError

            node_list.append((dst_id, yes_values))
        else:
            dst_id = instruction
            node_list.append((dst_id, copy.deepcopy(values_intervals)))

    instructions_dict[instr_id] = node_list


def intersect_intervals(values1, values2):
    new_values = {}
    for k in set(values1.keys()) | set(values2.keys()):
        new_s = None
        new_e = None
        s1, e1 = values1[k]
        s2, e2 = values2[k]
        if e2 < s1 or e1 < s2:
            return []
        else:
            if s2 <= s1 <= e2:
                new_s = s1
            elif s1 <= s2 <= e1:
                new_s = s2

            if s2 <= e1 <= e2:
                new_e = e1
            elif s1 <= e2 <= e1:
                new_e = e2

        new_values[k] = [new_s, new_e]
    return new_values


leaves = []
for node in instructions_dict:
    for leaf_id, values in instructions_dict[node]:
        leaves.append((leaf_id, (node, values)))

a_leaves = [(node, values) for (leaf_id, (node, values)) in leaves if leaf_id == "A"]

# Find all "A" leaves and traverse back the tree, updating the value intervals
scores = []
for origin_id, values1 in a_leaves:
    while origin_id != "in":
        tmp_leaves = [(node, values) for (leaf_id, (node, values)) in leaves if leaf_id == origin_id]
        (new_origin_id, values2), = tmp_leaves
        tmp_values = intersect_intervals(values1, values2)
        values1 = tmp_values
        origin_id = new_origin_id

    score = 1
    for k, v in values1.items():
        if not v:
            score *= 0
        else:
            x1, x2 = v
            delta = (x2 - x1 + 1)
            score *= delta
    scores.append(score)

print(scores)
print(sum(scores))

if __name__ == "__main__":
    pass