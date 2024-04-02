import re
import hashlib


def get_first_triplet(code):
    triplets = re.findall(r"(\w)\1{2,}", code)
    if triplets:
        return triplets[0]


salt = "ngcjuoqr"

for exec_id in [1, 2]:

    keys = []
    potential_keys = []
    idx = 0
    while len(keys) < 64 or (keys[63][0] + 1000) >= idx:
        code = hashlib.md5(f"{salt}{idx}".encode("utf8")).hexdigest()
        if exec_id == 2:
            for _ in range(2016):
                code = hashlib.md5(code.encode("utf8")).hexdigest()

        # check quintuplets for previous potential keys
        for old_idx, old_triplet, old_code in potential_keys:
            if idx - old_idx > 1001:
                continue
            elif old_triplet[0]*5 in code:
                if (old_idx, old_code) not in keys:
                    keys.append((old_idx, old_code))
                    keys = sorted(keys, key=lambda x: x[0])

        # check new triplets
        triplet = get_first_triplet(code)
        if triplet is not None:
            potential_keys.append((idx, triplet, code))
        idx += 1

    print(f"Part {exec_id} solution: {keys[63][0]}")


if __name__ == "__main__":
    pass