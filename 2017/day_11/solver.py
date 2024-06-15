
import collections


def parse_input():
    with open("input.txt") as f:
        step_directions = f.read().split(",")
    return step_directions


def get_combined_dirs(dir_name):
    directions = ["n", "ne", "se", "s", "sw", "nw"]
    dir_idx = directions.index(dir_name)
    opposite = directions[(dir_idx + 3) % 6]
    complementary = dict()
    complementary[directions[(dir_idx + 2) % 6]] = directions[(dir_idx + 1) % 6]
    complementary[directions[(dir_idx + 4) % 6]] = directions[(dir_idx + 5) % 6]
    return opposite, complementary


def run_steps(step_directions):
    dir_counter = collections.defaultdict(lambda: 0)
    num_steps = 0
    max_steps = 0
    for step_dir in step_directions:
        opposite, complementary = get_combined_dirs(step_dir)
        if dir_counter[opposite] > 0:
            dir_counter[opposite] -= 1
        else:
            for c_name, t_name in complementary.items():
                if dir_counter[c_name] > 0:
                    dir_counter[c_name] -= 1
                    dir_counter[t_name] += 1
                    break
            else:
                dir_counter[step_dir] += 1

        num_steps = sum(dir_counter.values())
        max_steps = max(max_steps, num_steps)

    return num_steps, max_steps


# ######## PART 1 & 2
step_directions = parse_input()
num_steps, max_steps = run_steps(step_directions)
print("Part 1 solution: ", num_steps)
print("Part 2 solution: ", max_steps)

if __name__ == "__main__":
    pass