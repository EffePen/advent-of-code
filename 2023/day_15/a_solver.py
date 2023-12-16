

with open("a_input.txt") as f:
    input_txt = f.read()


def hash_seq(seq):
    curr_value = 0
    for c in seq:
        ascii_val = ord(c)
        curr_value += ascii_val
        curr_value *= 17
        curr_value %= 256
    return curr_value


boxes = [[] for _ in range(256)]

values = []
for seq in input_txt.split(","):
    # part 1
    curr_value = hash_seq(seq)
    values.append(curr_value)

    # part 2
    mode = "-" if seq[-1] == "-" else "="
    if mode == "=":
        label = seq[:-2]
        lens = int(seq[-1])
    elif mode == "-":
        label = seq[:-1]
        lens = None
    else:
        raise ValueError

    box_idx = hash_seq(label)
    curr_box = boxes[box_idx]
    try:
        curr_box_label_idx = [l for l, _ in curr_box].index(label)
    except ValueError:
        curr_box_label_idx = -1

    if mode == "=":
        if curr_box_label_idx == -1:
            curr_box.append((label, lens))
        else:
            curr_box[curr_box_label_idx] = (label, lens)
    else:
        if curr_box_label_idx != -1:
            del curr_box[curr_box_label_idx]

    _nonempty_boxes = [(b_idx, box) for b_idx, box in enumerate(boxes) if box]
    a = 1


focusing_powers = []
for b_idx, box in enumerate(boxes):
    if not box:
        continue

    for l_idx, (label, lens) in enumerate(box, 1):
        curr_focusing_power = (b_idx + 1) * l_idx * lens
        focusing_powers.append(curr_focusing_power)

# part 1
print(sum(values))

# part 2
print(sum(focusing_powers))

if __name__ == "__main__":
    pass