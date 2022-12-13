from advent_of_code_2022.day_8 import (
    build_grid,
    calc_scenic_score,
    check_visible,
    count_perimeter,
    get_sight_lines,
    process,
)


def test_build_grid():
    data = """30373
25512
65332
33549
35390"""
    grid = build_grid(data)
    assert grid[4][4] == 0
    assert grid[0][0] == 3


def test_count_perimeter():
    data = """30373
25512
65332
33549
35390"""
    grid = build_grid(data)
    assert 16 == count_perimeter(grid)


def test_process():
    data = """30373
25512
65332
33549
35390"""
    assert 21 == process(data)


def test_check_visible():
    data = """30373
25512
65332
33549
35390"""
    grid = build_grid(data)
    sight_lines = get_sight_lines(1, 1, grid)
    assert check_visible(5, sight_lines) is True

    sight_lines = get_sight_lines(1, 2, grid)
    assert check_visible(5, sight_lines) is True

    sight_lines = get_sight_lines(1, 3, grid)

    assert check_visible(1, sight_lines) is False


def test_scenic_score():
    data = """30373
25512
65332
33549
35390"""
    grid = build_grid(data)
    sight_lines = get_sight_lines(3, 2, grid)
    assert calc_scenic_score(grid[3][2], sight_lines) == 8

    sight_lines = get_sight_lines(3, 2, grid)
    assert calc_scenic_score(grid[3][2], sight_lines) == 4
