

def parse_input():
    with open("input.txt") as f:
        bridges_txt = f.read().splitlines()
    bridges_tmp = [tuple([int(i) for i in e.split("/")]) for e in bridges_txt]
    bridges = [(b_idx, set(b), sum(b)) for b_idx, b in enumerate(bridges_tmp)]
    return bridges


def strongest_bridge(bridges, path=None, last_pins=0, tot_pins=0):
    path = path or []
    next_possible_bridges = [(b_idx, b, b_pins) for (b_idx, b, b_pins) in bridges
                             if last_pins in b and b_idx not in path]
    if not next_possible_bridges:
        return tot_pins
    else:
        new_tot_pins_list = []
        for (b_idx, b, b_pins) in next_possible_bridges:
            new_last_pins = b_pins - last_pins
            new_tot_pins = strongest_bridge(bridges, path=path + [b_idx], last_pins=new_last_pins, tot_pins=tot_pins + b_pins)
            new_tot_pins_list.append(new_tot_pins)
        max_pins = max(new_tot_pins_list)
        return max_pins


def longest_bridge(bridges, path=None, last_pins=0, tot_pins=0):
    path = path or []
    next_possible_bridges = [(b_idx, b, b_pins) for (b_idx, b, b_pins) in bridges
                             if last_pins in b and b_idx not in path]
    if not next_possible_bridges:
        return len(path), tot_pins
    else:
        max_len = 0
        max_pins = 0
        for (b_idx, b, b_pins) in next_possible_bridges:
            new_last_pins = b_pins - last_pins
            new_bridge_len, new_tot_pins = longest_bridge(bridges, path=path + [b_idx], last_pins=new_last_pins, tot_pins=tot_pins + b_pins)
            if new_bridge_len > max_len:
                max_len = new_bridge_len
                max_pins = new_tot_pins
            elif new_bridge_len == max_len:
                max_pins = max(max_pins, new_tot_pins)
        return max_len, max_pins


bridges = parse_input()


# ######## PART 1
score = strongest_bridge(bridges, path=[], last_pins=0, tot_pins=0)
print("Part 1 solution: ", score)

# ######## PART 2
_, score = longest_bridge(bridges, path=[], last_pins=0, tot_pins=0)
print("Part 2 solution: ", score)


if __name__ == "__main__":
    pass