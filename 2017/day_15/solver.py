

def generator_pt1(start, seed):
    next_num = start
    while True:
        next_num = (next_num * seed) % 2147483647
        yield next_num


def generator_pt2(start, seed, mod):
    next_num = start
    while True:
        next_num = (next_num * seed) % 2147483647
        if next_num % mod == 0:
            yield next_num


def generator_pt2_mersenne(start, seed, mod):
    # Exploiting Mersenne prime property
    # 2147483647 == 2**31 - 1
    # https://ariya.io/2007/02/modulus-with-mersenne-prime
    next_num = start
    while True:
        prod = (next_num * seed)
        n = 2147483647
        next_num = (prod & n) + (prod >> 31)
        next_num = next_num if next_num < n else next_num - n
        if next_num % mod == 0:
            yield next_num


def run_solution(generator_a, generator_b, n_rounds):
    last_16_digits_mask = (1 << 16) - 1
    counter = 0
    for _ in range(n_rounds):
        num_a = next(generator_a) & last_16_digits_mask
        num_b = next(generator_b) & last_16_digits_mask

        if (num_a & last_16_digits_mask) == (num_b & last_16_digits_mask):
            counter += 1

    return counter


gen_a_seed = 16807
gen_b_seed = 48271

gen_a_start = 516
gen_b_start = 190

# ######## PART 1
generator_a = generator_pt1(start=gen_a_start, seed=gen_a_seed)
generator_b = generator_pt1(start=gen_b_start, seed=gen_b_seed)
count = run_solution(generator_a, generator_b, n_rounds=40_000_000)
print("Part 1 solution: ", count)

# ######## PART 2
generator_a = generator_pt2_mersenne(start=gen_a_start, seed=gen_a_seed, mod=4)
generator_b = generator_pt2_mersenne(start=gen_b_start, seed=gen_b_seed, mod=8)
count = run_solution(generator_a, generator_b, n_rounds=5_000_000)
print("Part 2 solution: ", count)


if __name__ == "__main__":
    pass
