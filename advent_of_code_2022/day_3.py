from advent_of_code_2022.common import get_data_from_file


def sum_of_priorities(data, common_item_type_strategy):
    common_item_types = common_item_type_strategy(data)
    priorities = build_list_of_priorities(common_item_types)
    return sum(priorities)


def build_list_of_priorities(common_item_types):
    priorities = []
    for item_type in common_item_types:
        priority = calculate_priority_for_item_type(item_type)
        priorities.append(priority)
    return priorities


def common_item_type_part_1_strategy(data):
    return [find_common_item_type(item_list) for item_list in data.split("\n")]


def common_item_type_part_2_strategy(data):
    data_by_line = data.split("\n")
    group_of_sacks = build_list_of_three_sacks(data_by_line)
    return [find_3_common_item_type(group) for group in group_of_sacks]


def build_list_of_three_sacks(data_by_line):
    group_of_sacks = []
    current_sack_group = []
    for sack in data_by_line:
        current_sack_group.append(sack)
        if len(current_sack_group) == 3:
            group_of_sacks.append("\n".join(current_sack_group))
            current_sack_group = []
    return group_of_sacks


def calculate_priority_for_item_type(item_type):
    return priority_for_lower(item_type) if item_type.islower() else priority_for_upper(item_type)


def priority_for_upper(item_type):
    return ord(item_type) - 64 + 26


def priority_for_lower(item_type):
    return ord(item_type) - 96


def find_common_item_type(item_list):
    sack_1_items = item_list[: len(item_list) // 2]
    sack_2_items = item_list[len(item_list) // 2 :]
    for item in sack_1_items:
        if item in sack_2_items:
            return item


def find_3_common_item_type(data):
    sack_1, sack_2, sack_3 = data.split("\n")
    for item_type in sack_1:
        if is_item_in_all_sack(item_type, sack_2, sack_3):
            return item_type


def is_item_in_all_sack(item_type, sack_2, sack_3):
    return item_type in sack_2 and item_type in sack_3


def main(filename, strategy):
    file_data = get_data_from_file(filename)
    score = sum_of_priorities(file_data, strategy)

    print(f"The sum of priorities is {score}")


if __name__ in "__main__":
    main("day_3.txt", common_item_type_part_1_strategy)
    main("day_3.txt", common_item_type_part_2_strategy)
