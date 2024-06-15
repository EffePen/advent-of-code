
import functools


def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()
    return input_txt


def run_hashing(list_size, lengths, n_rounds=1):
    skip = 0
    idx = 0
    numbers_list = list(range(list_size))

    for _ in range(n_rounds):
        for l in lengths:
            if l > list_size:
                raise ValueError

            if idx + l < list_size:
                sub_list = numbers_list[idx:idx+l]
                numbers_list = numbers_list[:idx] + sub_list[::-1] + numbers_list[idx+l:]
                assert len(numbers_list) == list_size
            else:
                r = (idx + l) % list_size
                sub_list = numbers_list[idx:] + numbers_list[:r]
                sub_list = sub_list[::-1]
                numbers_list = sub_list[l-r:] + numbers_list[r:idx] + sub_list[:l-r]
                assert len(numbers_list) == list_size
            idx = (idx + l + skip) % list_size
            skip += 1

    return numbers_list


input_txt = parse_input()
list_size = 256

# ######## PART 1
lengths = [int(e) for e in input_txt.split(",")]
numbers_list = run_hashing(list_size=list_size, lengths=lengths)
score = numbers_list[0]*numbers_list[1]
print("Part 1 solution: ", score)


# ######## PART 2
lengths = [ord(c) for c in input_txt] + [17, 31, 73, 47, 23]
numbers_list = run_hashing(list_size=list_size, lengths=lengths, n_rounds=64)
reduced_numbers_list = [functools.reduce(lambda a,b: a^b, numbers_list[idx*16:(idx+1)*16])
                        for idx in range(list_size // 16)]
reduced_hex_string = "".join([f"{n:02x}" for n in reduced_numbers_list])
print("Part 2 solution: ", reduced_hex_string)


if __name__ == "__main__":
    pass