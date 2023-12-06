
import math

with open('a_input.txt') as f:
    input_txt = f.read()

lines = input_txt.splitlines()

times = [int("".join([e for e in lines[0].split()[1:]]))]
dists = [int("".join([e for e in lines[1].split()[1:]]))]

score = 1
for t, d in zip(times, dists):
    # solve eq
    disc = (t**2 - 4*d)**0.5
    max_w = (-t - disc) / -2
    min_w = (-t + disc) / -2

    int_max_w = math.floor(max_w)
    int_min_w = math.ceil(min_w)

    if math.floor(max_w) == max_w:
        int_max_w -= 1
    if math.floor(min_w) == min_w:
        int_min_w += 1

    print(min_w, max_w, max_w-min_w)
    print(int_min_w, int_max_w, int_max_w-int_min_w)
    n_sols = int_max_w - int_min_w + 1

    score *= n_sols

print(score)

if __name__ == "__main__":
    pass