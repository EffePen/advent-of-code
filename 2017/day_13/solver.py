

def parse_input():
    with open("input.txt") as f:
        input_lines = f.read().splitlines()
    layers = dict([(int(e) for e in l.split(": ")) for l in input_lines])
    return layers


def get_hit_score(layers, delay=0):
    hit_score = 0
    for l_idx, l_len in layers.items():
        l_period = 2 * (l_len - 1)
        if (l_idx+delay) % l_period == 0:
            hit_score += l_idx*l_len
    return hit_score


def has_hits(layers, delay=0):
    for l_idx, l_len in layers.items():
        l_period = 2 * (l_len - 1)
        if (l_idx+delay) % l_period == 0:
            return True
    return False


def get_escape_delay(layers):
    delay = 0
    while True:
        if not has_hits(layers, delay):
            break
        else:
            delay += 1
    return delay


layers = parse_input()


# ######## PART 1
hit_score = get_hit_score(layers)
print("Part 1 solution: ", hit_score)

# ######## PART 2
delay = get_escape_delay(layers)
print("Part 2 solution: ", delay)


if __name__ == "__main__":
    pass