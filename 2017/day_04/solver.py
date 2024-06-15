

def parse_input():
    with open("input.txt") as f:
        passphrases_list = f.readlines()
    return passphrases_list


def is_valid_passphrase_p1(passphrase):
    passphrase_words = passphrase.split()
    return len(passphrase_words) == len(set(passphrase_words))


def is_valid_passphrase_p2(passphrase):
    passphrase_words = passphrase.split()
    # sort each word letters and then check if there are duplicates
    passphrase_sorted_words = ["".join(sorted(w)) for w in passphrase_words]
    return len(passphrase_sorted_words) == len(set(passphrase_sorted_words))


passphrases_list = parse_input()

# ######## PART 1
valid_passphrases = [pp for pp in passphrases_list if is_valid_passphrase_p1(pp)]
print("Part 1 solution: ", len(valid_passphrases))


# ######## PART 2
valid_passphrases = [pp for pp in passphrases_list if is_valid_passphrase_p2(pp)]
print("Part 2 solution: ", len(valid_passphrases))


if __name__ == "__main__":
    pass