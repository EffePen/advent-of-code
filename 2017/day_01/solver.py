

def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    digits_list = [int(e) for e in input_txt]
    return digits_list


digits_list = parse_input()
list_len = len(digits_list)

# ######## PART 1& 2
solution1 = 0
solution2 = 0
for i in range(list_len):
    if digits_list[i] == digits_list[(i+1) % list_len]:
        solution1 += digits_list[i]
    if digits_list[i] == digits_list[(i+list_len//2) % list_len]:
        solution2 += digits_list[i]

print("Part 1 solution: ", solution1)
print("Part 2 solution: ", solution2)


if __name__ == "__main__":
    pass