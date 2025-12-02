

def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    pairs = [e.split("-") for e in input_txt.split(",")]
    return pairs


def solve_pt1(pairs):
    score = 0
    weird_numbers = []
    for min_str, max_str in pairs:
        min = int(min_str)
        max = int(max_str)
        # if the min_str number of digits is odd, change min_str
        if len(min_str) % 2:
            min_str = "1" + "0" * len(min_str)
        weird_number_half = int(min_str[:len(min_str)//2])
        weird_number_str = str(weird_number_half) * 2
        weird_number = int(weird_number_str)
        while weird_number <= max:
            if weird_number >= min:
                score += weird_number
                weird_numbers.append(weird_number)
            weird_number_half += 1
            weird_number_str = str(weird_number_half) * 2
            weird_number = int(weird_number_str)
    return score


def solve_pt2(pairs):
    weird_numbers = []
    for min_str, max_str in pairs:
        min_val = int(min_str)
        max_val = int(max_str)

        for num_parts in range(2, max(3, len(max_str)+1)):
            tmp_min_str = min_str
            if len(tmp_min_str) % num_parts:
                # if the min_str number of digits is non-divisible by num_parts, change min_str
                tmp_min_str = "1" + "0" * (len(tmp_min_str) + len(tmp_min_str) % num_parts - 1)
            weird_number_part = int(tmp_min_str[:len(tmp_min_str)//num_parts])
            weird_number_str = str(weird_number_part) * num_parts
            weird_number = int(weird_number_str)
            while weird_number <= max_val:
                if weird_number >= min_val:
                    weird_numbers.append(weird_number)
                weird_number_part += 1
                weird_number_str = str(weird_number_part) * num_parts
                weird_number = int(weird_number_str)
    score = sum(set(weird_numbers))
    return score


# PARSE INPUT
pairs = parse_input()

# PART 1
score = solve_pt1(pairs)
print(f"Part 1 solution: {score}")


# PART 2
score = solve_pt2(pairs)
print(f"Part 2 solution: {score}")


if __name__ == "__main__":
    pass