

with open('a_input.txt') as f:
    input_txt = f.read()

seeds_raw, maps_raw = input_txt.split("\n\n", 1)
seeds = [int(s) for s in seeds_raw.split("seeds: ")[1].strip().split()]

items_map = {}
values_mapping = {}
for m_raw in maps_raw.split("\n\n"):
    # get items mapping
    source_item, destination_item = m_raw.split(" map:")[0].strip().split("-to-")

    # get value mapping
    values_mapping[source_item] = []
    for map_line in m_raw.split(" map:")[1].strip().split("\n"):
        destination_start, source_start, m_range = [int(e) for e in map_line.split()]
        values_mapping[source_item].append((source_start, destination_start, m_range, destination_item))


def get_next(item, value):
    next_value = value
    for source_start, destination_start, m_range, destination_item in values_mapping[item]:
        if value >= source_start and value < source_start + m_range:
            next_value = destination_start + (value - source_start)
    return destination_item, next_value


locations = []
for value in seeds:
    item = 'seed'
    while item != "location":
        item, value = get_next(item, value)
    locations.append(value)

print(min(locations))



if __name__ == "__main__":
    pass