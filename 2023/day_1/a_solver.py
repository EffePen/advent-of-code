
import re
import random


with open('a_input.txt') as f:
    input_txt = f.read()

# ############# part A
#numbers = []
#input_txt_digits_only = re.sub("[^0-9\n]", "", input_txt)
#for l in input_txt_digits_only.splitlines():
#    number = f"{l[0]}{l[-1]}"
#    numbers.append(int(number))

#print("Solution a:", sum(numbers), len(numbers))


# ############# part B
numbers_dict = {
    "one": "1",
    "two":   "2",
    "three": "3",
    "four":  "4",
    "five":  "5",
    "six":   "6",
    "seven": "7",
    "eight": "8",
    "nine":  "9",
}

numbers = []
lines = input_txt.splitlines()
random.shuffle(lines)

for l in lines:
    min_idx = len(l)
    max_idx = -1
    l_digit = ""
    r_digit = ""
    for d_txt, d_digit in numbers_dict.items():
        # left
        d_l_index = min(l.find(d_txt) if l.find(d_txt) != -1 else min_idx,\
                        l.find(d_digit) if l.find(d_digit) != -1 else min_idx)
        if d_l_index < min_idx:
            l_digit = d_digit
            min_idx = d_l_index
        # right
        d_r_index = max(l.rfind(d_txt), l.rfind(d_digit))
        if d_r_index > max_idx:
            r_digit = d_digit
            max_idx = d_r_index
    number = f"{l_digit}{r_digit}"
    numbers.append(int(number))

print("Solution b:", sum(numbers), len(numbers))

if __name__ == "__main__":
    pass