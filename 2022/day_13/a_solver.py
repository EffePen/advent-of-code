

with open("a_input.txt") as f:
    input_txt = f.read()


def format_types(l_val, r_val):
    if type(l_val) != type(r_val):
        if type(l_val) == int:
            l_val = [l_val]
        if type(r_val) == int:
            r_val = [r_val]

    return l_val, r_val


def custom_less_than(l_val, r_val):
    l_val, r_val = format_types(l_val, r_val)

    if type(l_val) == type(r_val) == int:
        is_ordered = int_check(l_val, r_val)
    elif type(l_val) == type(r_val) == list:
        is_ordered = list_check(l_val, r_val)
    else:
        raise TypeError
    return is_ordered


def custom_less_than_mod(l_val, r_val):
    cmp = custom_less_than(l_val, r_val)
    if cmp is True:
        return -1
    elif cmp is False:
        return 1
    else:
        return 0


def int_check(l_val, r_val):
    if l_val < r_val:
        return True
    elif l_val > r_val:
        return False
    else:
        return None


def list_check(l_val, r_val):
    l_len = len(l_val)
    r_len = len(r_val)

    for idx in range(min(l_len, r_len)):
        is_ordered = custom_less_than(l_val[idx], r_val[idx])
        if is_ordered is not None:
            return is_ordered

    if l_len < r_len:
        is_ordered = True
    elif l_len > r_len:
        is_ordered = False
    else:
        is_ordered = None

    return is_ordered


score = 0
full_packets_list = [[[2]], [[6]]]
for p_idx, pair_txt in enumerate(input_txt.split("\n\n"), 1):
    left_txt, right_txt = pair_txt.splitlines()
    lval = eval(left_txt)
    rval = eval(right_txt)
    full_packets_list.extend([lval, rval])

    is_ord = custom_less_than(lval, rval)
    if is_ord:
        score += p_idx

print(score)

from functools import cmp_to_key
full_packets_list = sorted(full_packets_list, key=cmp_to_key(custom_less_than_mod))

score = 1
for idx, e in enumerate(full_packets_list, 1):
    if str(e) in ("[[2]]", "[[6]]"):
        score *= idx
print(score)

if __name__ == "__main__":
    pass
