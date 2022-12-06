from advent_of_code_2022.day_6 import process


def test_find_start_packet():
    data = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""
    assert 7 == process(data, 4)

    data = """bvwbjplbgvbhsrlpgdmjqwftvncz"""
    assert 5 == process(data, 4)

    assert 6 == process("nppdvjthqldpwncqszvftbrmjlhg", 4)
    assert 10 == process("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4)
    assert 11 == process("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4)

    assert 19 == process("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14)
    assert 23 == process("bvwbjplbgvbhsrlpgdmjqwftvncz", 14)
