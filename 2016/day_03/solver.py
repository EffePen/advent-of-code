

import itertools


def parse_input_part_1():
    with open("input.txt") as f:
        input_txt = f.read()
    triangles = [[int(l) for l in e.strip().split()] for e in input_txt.splitlines()]
    return triangles


def parse_input_part_2():
    with open("input.txt") as f:
        input_txt = f.read()
    not_triangles = [[int(l) for l in e.strip().split()] for e in input_txt.splitlines()]
    columns = list(zip(*not_triangles))
    tot_sides = list(itertools.chain.from_iterable(columns))
    triangles = [tot_sides[3*idx:(idx+1)*3] for idx in range(len(tot_sides)//3)]
    return triangles


def count_possibile_triangles(triangles):
    counter = 0
    for sides in triangles:
        if all([sides[idx] < (sides[(idx + 1) % len(sides)] + sides[(idx + 2) % len(sides)])
                for idx in range(3)]):
            counter += 1
    return counter


# PART 1
triangles = parse_input_part_1()
counter = count_possibile_triangles(triangles)
print(f"Part 1 solution: {counter}")


# PART 2
triangles = parse_input_part_2()
counter = count_possibile_triangles(triangles)
print(f"Part 2 solution: {counter}")

if __name__ == "__main__":
    pass