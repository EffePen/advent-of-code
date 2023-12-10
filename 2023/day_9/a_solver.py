
import re

with open("a_input.txt") as f:
    input_txt = f.read()

sequences = [[int(e) for e in l.split()] for l in input_txt.splitlines()]

pred_prev_values = []
pred_next_values = []
for sequence in sequences:
    layers = [sequence]

    while not all([e == 0 for e in layers[-1]]):
        # append diff of previous layer element pairs
        new_layer = [(layers[-1][idx+1] - layers[-1][idx]) for idx in range(len(layers[-1])-1)]
        layers.append(new_layer)

    # sum last values in layers (..., accel to speed to distance)
    curr_last_momentum = 0
    curr_first_momentum = 0
    for layer in layers[::-1]:
        curr_last_momentum = layer[-1] + curr_last_momentum
        curr_first_momentum = layer[0] - curr_first_momentum

    pred_prev_values.append(curr_first_momentum)
    pred_next_values.append(curr_last_momentum)


print(sum(pred_next_values))
print(sum(pred_prev_values))

if __name__ == "__main__":
    pass
