from advent_of_code_2022.day_9 import parse_instructions, process


def test_process():
    data = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
    assert 13 == process(data, 1)


def test_parse_instructions():
    data = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
    instructions = parse_instructions(data)
    assert len(instructions) == 8
    assert instructions[0] == ("R", 4)
