from advent_of_code_2022.day_4 import find_overlaps, part_1_strategy, part_2_strategy


def test_find_overlaps():
    data = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
    assert 2 == find_overlaps(data, part_1_strategy)

    assert 4 == find_overlaps(data, part_2_strategy)
