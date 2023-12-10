
import math

with open("a_input.txt") as f:
    input_txt = f.read()

direct_map = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
reverse_map = {v: k for k, v in direct_map.items()}

values = []
for line in input_txt.splitlines():
    line_val = 0
    for c_idx, char in enumerate(line[::-1]):
        line_val += direct_map[char] * (5**c_idx)
    values.append(line_val)


tot_val = sum(values)

max_power = math.floor(math.log(tot_val, 5))
factors = [0]*(max_power+1)

for curr_power in range(max_power+1)[::-1]:
    max_add_lower_power = sum([2 * 5**lower_power for lower_power in range(curr_power)])

    for v in [2, 1, 0, -1, -2]:
        factors[curr_power] = v
        approx_val = sum([e*5**idx for idx, e in enumerate(factors)])

        if abs(approx_val - tot_val) <= max_add_lower_power:
            break

approx_val = sum([e*5**idx for idx, e in enumerate(factors)])
assert approx_val == tot_val

print("".join([reverse_map[f] for f in factors[::-1]]))


if __name__ == "__main__":
    pass