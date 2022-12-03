from advent_of_code_2022.day_3 import (
    calculate_priority_for_item_type,
    common_item_type_part_1_strategy,
    common_item_type_part_2_strategy,
    find_3_common_item_type,
    find_common_item_type,
    sum_of_priorities,
)


def test_sum_of_priorities():
    data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

    assert sum_of_priorities(data, common_item_type_part_1_strategy) == 157

    assert sum_of_priorities(data, common_item_type_part_2_strategy) == 70


def test_find_common_item_type():
    item_list = "vJrwpWtwJgWrhcsFMMfFFhFp"
    assert "p" == find_common_item_type(item_list)

    item_list = "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"
    assert "L" == find_common_item_type(item_list)

    item_list = "PmmdzqPrVvPwwTWBwg"
    assert "P" == find_common_item_type(item_list)

    item_list = "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn"
    assert "v" == find_common_item_type(item_list)

    item_list = "ttgJtRGJQctTZtZT"
    assert "t" == find_common_item_type(item_list)

    item_list = "CrZsJsPPZsGzwwsLwLmpwMDw"
    assert "s" == find_common_item_type(item_list)


def test_calculate_priority_for_item_type():
    assert 16 == calculate_priority_for_item_type("p")

    assert 38 == calculate_priority_for_item_type("L")


def test_find_3_common_item_type():
    data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg"""
    assert "r" == find_3_common_item_type(data)

    data = """wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
    assert "Z" == find_3_common_item_type(data)
