
input_txt = "10011111011011001"


# PART 1
disc_size = 272

# calc data
data = [bool(int(c)) for c in input_txt]
while len(data) < disc_size:
    data += [0] + [(not e) for e in data[::-1]]
data = data[:disc_size]

# calc checksum
checksum = data
while True:
    assert len(checksum) % 2 == 0
    checksum = [checksum[2*idx] == checksum[2*idx+1] for idx in range(len(checksum) // 2)]
    if len(checksum) % 2 != 0:
        break
print(f"Part 1 solution: {''.join(map(lambda x: str(int(x)), checksum))}")


# PART 2
disc_size = 35651584

# calc data
data = [bool(int(c)) for c in input_txt]
while len(data) < disc_size:
    data += [0] + [(not e) for e in data[::-1]]
data = data[:disc_size]

# calc checksum
checksum = data
while True:
    assert len(checksum) % 2 == 0
    checksum = [checksum[2*idx] == checksum[2*idx+1] for idx in range(len(checksum) // 2)]
    if len(checksum) % 2 != 0:
        break
print(f"Part 2 solution: {''.join(map(lambda x: str(int(x)), checksum))}")


if __name__ == "__main__":
    pass