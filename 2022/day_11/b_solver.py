

import math

with open("a_input.txt") as f:
    input_txt = f.read()

monkeys = {}
for monkey_info in input_txt.split("\n\n"):
    m_lines = monkey_info.splitlines()

    monkey_id = int(m_lines[0].split("Monkey ")[-1].replace(":", ""))
    item_levels = [int(e) for e in m_lines[1].split("Starting items: ")[-1].strip().split(", ")]
    op, num = m_lines[2].split("new = old ")[-1].strip().split()
    divisible_factor = int(m_lines[3].split("divisible by ")[-1].strip())
    dst_true  = int(m_lines[4].split("to monkey ")[-1])
    dst_false = int(m_lines[5].split("to monkey ")[-1])

    monkeys[monkey_id] = [item_levels, (op, num), (divisible_factor, dst_true, dst_false)]

common_factor = 1
for m_id in monkeys:
    common_factor *= monkeys[m_id][2][0]

monkeys_inspections = {m: 0 for m in monkeys}

for _ in range(10000):
    for idx in range(len(monkeys)):
        while monkeys[idx][0]:
            item_level = monkeys[idx][0].pop()

            # inspect
            op, num = monkeys[idx][1]
            if op == "+":
                item_level += int(num)
            elif op == "*":
                if num == "old":
                    item_level *= item_level
                else:
                    item_level *= int(num)
            else:
                raise RuntimeError

            monkeys_inspections[idx] += 1

            # lower level
            # solved searching the solution.
            item_level = item_level % common_factor

            # throw
            factor, dst_true, dst_false = monkeys[idx][2]
            dst_idx = dst_true if item_level % factor == 0 else dst_false
            monkeys[dst_idx][0].append(item_level)

score = 1
top_n = 2
for n in sorted(monkeys_inspections.values(), reverse=True)[:top_n]:
    score *= n
print(score)

if __name__ == "__main__":
    pass
