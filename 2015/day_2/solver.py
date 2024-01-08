
def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    sizes = [list(map(int, e.split("x"))) for e in input_txt.splitlines()]
    return sizes


sizes = parse_input()

# part 1
areas = [(2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)) for l, w, h in sizes]
print("Part 1:", sum(areas))

# part 2
lengths = []
for tmp_sizes in sizes:
    l, w, h = tmp_sizes
    sorted_sizes = sorted(tmp_sizes)
    lengths.append(2*sorted_sizes[0] + 2*sorted_sizes[1] + l*w*h)
print("Part 2:", sum(lengths))

if __name__ == "__main__":
    pass
