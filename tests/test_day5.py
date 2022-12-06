from advent_of_code_2022.day_5 import get_crane_status, get_move_instructions, part_1_strategy, part_2_strategy, process


def test_build_crane_status():
    data = """    [D]    # noqa:W291
[N] [C]    # noqa:W291
[Z] [M] [P]
 1   2   3 """
    crane_status = get_crane_status(data)

    assert list(crane_status[1]) == ["Z", "N"]
    assert list(crane_status[2]) == ["M", "C", "D"]
    assert list(crane_status[3]) == ["P"]


def test_get_move_instructions():
    data = """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

    instructions = get_move_instructions(data)
    assert [(1, 2, 1), (3, 1, 3), (2, 2, 1), (1, 1, 2)] == instructions


def test_process():
    data = """    [D]    # noqa:W291
[N] [C]    # noqa:W291
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

    assert "CMZ" == process(data, part_1_strategy)

    assert "MCD" == process(data, part_2_strategy)
