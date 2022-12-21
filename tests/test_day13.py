from advent_of_code_2022.day_13 import calculate_sum_of_pair, compare, get_pairs, multiply_divider_indices


def test_calculate_sum_of_pair():
    data = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""
    assert 13 == calculate_sum_of_pair(data)


def test_get_pairs():
    data = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]"""
    pairs = get_pairs(data)
    assert len(pairs) == 2
    assert pairs[0][0] == [1, 1, 3, 1, 1]


def test_compare():
    assert compare(1, 1) is None
    assert -1 == compare(1, 2)
    assert 1 == compare(2, 1)
    assert -1 == compare([1, 1, 3, 1, 1], [1, 1, 5, 1, 1])
    assert -1 == compare([[1], [2, 3, 4]], [[1], 4])
    assert -1 == compare([[4, 4], 4, 4], [[4, 4], 4, 4, 4])
    assert 1 == compare([7, 7, 7, 7], [7, 7, 7])
    assert -1 == compare([], [3])
    assert 1 == compare([[[]]], [[]])
    assert 1 == compare([1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9])


def test_part2():
    data = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""
    assert 140 == multiply_divider_indices(data)
