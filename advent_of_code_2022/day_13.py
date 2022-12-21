import ast
from functools import cmp_to_key
from itertools import zip_longest

from advent_of_code_2022.common import get_data_from_file


def calculate_sum_of_pair(data):
    pairs = get_pairs(data)
    results = [compare(*pair) for pair in pairs]
    indices = [index + 1 for index, result in enumerate(results) if result == -1]
    return sum(indices)


def get_pairs(data):
    pairs = []
    for pair_string in data.split("\n\n"):
        pair_list = [ast.literal_eval(item) for item in pair_string.split("\n")]
        pairs.append(pair_list)
    return pairs


def is_all_ints(left, right):
    return isinstance(left, int) and isinstance(right, int)


def is_all_list(left, right):
    return isinstance(left, list) and isinstance(right, list)


def main(filename):
    data = get_data_from_file(filename)
    sum_of_pair = calculate_sum_of_pair(data)
    print(f"The result is {sum_of_pair}")

    result = multiply_divider_indices(data)
    print(f"result: {result}")


def multiply_divider_indices(data):
    pairs = get_pairs(data)
    divider_1, divider_2 = [[2]], [[6]]
    flat_list = create_flat_list_of_pairs(pairs)
    sorted_packets = sort_pairs_with_dividers(divider_1, divider_2, flat_list)
    return (sorted_packets.index(divider_1) + 1) * (sorted_packets.index(divider_2) + 1)


def sort_pairs_with_dividers(divider_1, divider_2, flat_list):
    sorted_packets = sorted([*flat_list, divider_1, divider_2], key=cmp_to_key(compare))
    return sorted_packets


def create_flat_list_of_pairs(pairs):
    flat_list = [item for sublist in pairs for item in sublist]
    return flat_list


def compare(left, right):
    if left is None:
        return -1
    if right is None:
        return 1

    if is_all_ints(left, right):
        return process_all_ints(left, right)
    elif is_all_list(left, right):
        return process_all_lists(left, right)
    else:
        return process_mixed(left, right)


def process_mixed(left, right):
    new_left = [left] if isinstance(left, int) else left
    new_right = [right] if isinstance(right, int) else right
    if not isinstance(new_left, list) or not isinstance(new_right, list):
        raise Exception(type(new_left), type(new_right))
    return compare(new_left, new_right)


def process_all_lists(left, right):
    for new_left, new_right in zip_longest(left, right):
        if (result := compare(new_left, new_right)) is not None:
            return result
    return None


def process_all_ints(left, right):
    if left < right:
        return -1
    elif left > right:
        return 1
    return None


if __name__ in "__main__":
    main("day_13.txt")
