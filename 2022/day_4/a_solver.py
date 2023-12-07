
def get_intersection(interval1, interval2):
    new_min = max(interval1[0], interval2[0])
    new_max = min(interval1[1], interval2[1])
    return (new_min, new_max) if new_min <= new_max else None


with open('a_input.txt') as f:
    input_txt = f.read()


full_overlapping = []
overlapping = []

for pair_line in input_txt.splitlines():
    r1, r2 = [tuple([int(e) for e in elf_range_str.split("-")])
              for elf_range_str in pair_line.split(",")]

    intersection = get_intersection(r1, r2)
    if intersection in (r1, r2):
        full_overlapping.append((r1, r2))

    if intersection is not None:
        overlapping.append((r1, r2))

print(len(full_overlapping))
print(len(overlapping))

if __name__ == "__main__":
    pass
