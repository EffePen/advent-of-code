
from utils import *


with open('a_input.txt') as f:
    input_txt = f.read()

seeds_raw, maps_raw = input_txt.split("\n\n", 1)
seeds_tmp = seeds_raw.split("seeds: ")[1].strip().split()
seed_intervals = [(int(seeds_tmp[2 * idx]), int(seeds_tmp[2 * idx]) + int(seeds_tmp[2 * idx + 1])) for idx in range(len(seeds_tmp) // 2)]

values_mapping = get_values_mapping(maps_raw)

locations = []
current_item = "seed"
current_intervals = seed_intervals
while current_item != "location":
    next_item, _ = values_mapping[current_item]
    next_intervals = []
    # for each interval, get mapped next intervals
    for interval in current_intervals:
        _, tmp_next_intervals = get_next_ranges(current_item, interval, values_mapping)
        next_intervals.extend(tmp_next_intervals)

    # Get min interval start for locations
    if next_item == "location":
        print(min([e[0] for e in next_intervals if e[0] != 0 and e[1] != 0]))

    current_item = next_item
    current_intervals = next_intervals


if __name__ == "__main__":
    pass