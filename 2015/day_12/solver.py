
import json


def parse_input():
    with open("input.json") as f:
        input_dict = json.load(f)
    return input_dict


def traverse_p1(obj, numbers_list):
    if isinstance(obj, int):
        numbers_list.append(obj)
    elif isinstance(obj, list):
        for sub_obj in obj:
            traverse_p1(sub_obj, numbers_list)
    elif isinstance(obj, dict):
        for sub_obj in obj.values():
            traverse_p1(sub_obj, numbers_list)
    elif isinstance(obj, str):
        pass
    else:
        raise ValueError


def traverse_p2(obj, numbers_list):
    if isinstance(obj, int):
        numbers_list.append(obj)
    elif isinstance(obj, list):
        for sub_obj in obj:
            traverse_p2(sub_obj, numbers_list)
    elif isinstance(obj, dict):
        if "red" not in list(obj.values()):
            for sub_obj in obj.values():
                traverse_p2(sub_obj, numbers_list)
    elif isinstance(obj, str):
        pass
    else:
        raise ValueError


# part 1
input_dict = parse_input()
numbers_list = []
traverse_p1(input_dict, numbers_list)

print("Part 1:", sum(numbers_list))

# part 2
input_dict = parse_input()
numbers_list = []
traverse_p2(input_dict, numbers_list)

print("Part 2:", sum(numbers_list))


if __name__ == "__main__":
    pass
