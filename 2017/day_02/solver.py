

def parse_input():
    with open("input.txt") as f:
        input_txt = f.readlines()
    number_lists = [[int(e) for e in l.split()] for l in input_txt]
    return number_lists


number_lists = parse_input()

# ######## PART 1
solution1 = 0
for l in number_lists:
    solution1 += max(l) - min(l)

print("Part 1 solution: ", solution1)


# ######## PART 2
solution2 = 0
for l in number_lists:
    for n1_idx, n1 in enumerate(l):
        for n2 in l[n1_idx+1:]:
            if n1 % n2 == 0:
                solution2 += n1 / n2
            if n2 % n1 == 0:
                solution2 += n2 / n1
print("Part 2 solution: ", solution2)


if __name__ == "__main__":
    pass