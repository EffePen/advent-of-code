
import copy


def parse_input():
    with open("input.txt") as f:
        transformations_str = f.read().splitlines()

    transformation = {}
    for transformation_str in transformations_str:
        src, dst = transformation_str.split(" => ")
        src_arr = [list(e) for e in src.split("/")]
        # simple & rotated
        new_arr = copy.deepcopy(src_arr)
        for _ in range(4):
            new_arr = rotate_array_90deg(new_arr)
            transformation["/".join(["".join(e) for e in new_arr])] = dst
        # flipped h & rotated
        new_arr = flip_array_h(src_arr)
        for _ in range(4):
            new_arr = rotate_array_90deg(new_arr)
            transformation["/".join(["".join(e) for e in new_arr])] = dst
        # flipped v & rotated
        new_arr = flip_array_v(src_arr)
        for _ in range(4):
            new_arr = rotate_array_90deg(new_arr)
            transformation["/".join(["".join(e) for e in new_arr])] = dst

    return transformation


def rotate_array_90deg(arr):
    arr = list(zip(*arr[::-1]))
    return arr


def flip_array_v(arr):
    arr = arr[::-1]
    return arr


def flip_array_h(arr):
    arr = [l[::-1] for l in arr]
    return arr


def transform_pattern(initial_pattern, transformations, n_iterations):
    array = initial_pattern.split("/")
    for _ in range(n_iterations):
        size = len(array)
        if size % 2 == 0:
            splits = size // 2
            split_size = 2
        elif size % 3 == 0:
            splits = size // 3
            split_size = 3
        else:
            raise ValueError

        new_array = []
        for v_split_idx in range(splits):
            new_sub_arrays = []
            r0, r1 = (v_split_idx * split_size, (v_split_idx + 1) * split_size)
            for h_split_idx in range(splits):
                c0, c1 = (h_split_idx * split_size, (h_split_idx + 1) * split_size)
                sub_array = [r[c0:c1] for r in array[r0:r1]]
                sub_pattern = "/".join(sub_array)
                new_sub_pattern = transformations[sub_pattern]
                new_sub_array = new_sub_pattern.split("/")
                new_sub_arrays.append(new_sub_array)
            new_array += ["".join(r_parts) for r_parts in zip(*new_sub_arrays)]
        array = new_array
    return array


transformations = parse_input()
initial_pattern = ".#./..#/###"


# ######## PART 1
n_iterations = 5
array = transform_pattern(initial_pattern, transformations, n_iterations)
print("Part 1 solution: ", "".join(array).count("#"))


# ######## PART 2
n_iterations = 18
array = transform_pattern(initial_pattern, transformations, n_iterations)
print("Part 2 solution: ", "".join(array).count("#"))


if __name__ == "__main__":
    pass