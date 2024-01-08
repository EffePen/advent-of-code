
import hashlib

input_txt = "iwrupvqb"

# part 1
idx = 0
while True:
    idx += 1
    key = f"{input_txt}{idx}"
    hash = hashlib.md5(key.encode()).hexdigest()
    if hash.startswith("00000"):
        break

print("Part 1:", idx)


# part 2
idx = 0
while True:
    idx += 1
    key = f"{input_txt}{idx}"
    hash = hashlib.md5(key.encode()).hexdigest()
    if hash.startswith("000000"):
        break

print("Part 2:", idx)

if __name__ == "__main__":
    pass
