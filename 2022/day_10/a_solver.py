
with open("a_input.txt") as f:
    input_txt = f.read()


valx = 1
values = [1]
chars = []

for line in input_txt.splitlines():
    if line == "noop":
        values.append(valx)
    else:
        increase = int(line.split()[1])
        values.extend([valx, valx + increase])
        valx += increase

# Print score part 1
scores = []
cycle = 20
while cycle < len(values) - 1:
    scores.append(cycle * values[cycle-1])
    cycle += 40

print(sum(scores))

# Draw letters part 2
for cycle_idx in range(1, len(values)):
    pixel_idx = cycle_idx - 1
    pixel_idx -= 40 * (pixel_idx // 40)
    sprite_position = values[cycle_idx-1]
    if sprite_position-1 <= pixel_idx <= sprite_position+1:
        chars.append("#")
    else:
        chars.append(".")

cycle = 1
while cycle < len(chars) - 1:
    print("".join(chars[cycle: cycle+40]))
    cycle += 40


if __name__ == "__main__":
    pass
