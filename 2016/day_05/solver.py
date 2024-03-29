

import hashlib


input_txt = "reyedfim"

#code1_digits = []
#idx = 0
#while len(code1_digits) < 8:
#    hash = hashlib.md5(f"{input_txt}{idx}".encode("utf-8")).hexdigest()
#    if hash.startswith("00000"):
#        code1_digits.append(hash[5])
#    idx += 1


code2_positions = set()
code2_digits = [None]*8
idx = 0
while len(code2_positions) < 8:
    hash = hashlib.md5(f"{input_txt}{idx}".encode("utf-8")).hexdigest()
    if hash.startswith("00000"):
        try:
            position = int(hash[5])
            if position < 8 and code2_digits[position] is None:
                code2_digits[position] = hash[6]
                code2_positions.add(position)
        except ValueError:
            pass
    idx += 1



# PART 1
#print(f"Part 1 solution: {''.join(code1_digits)}")

# PART 2
print(f"Part 1 solution: {''.join(code2_digits)}")

if __name__ == "__main__":
    pass