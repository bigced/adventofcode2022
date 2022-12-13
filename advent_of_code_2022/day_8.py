from functools import reduce

from advent_of_code_2022.common import get_data_from_file


def build_grid(data):
    grid = [build_row(line) for line in data.split("\n")]
    return grid


def build_row(line):
    row = [int(c) for c in line]
    return row


def count_perimeter(grid):
    return (len(grid) + len(grid[0])) * 2 - 4


def process(data):
    grid = build_grid(data)
    visible = count_perimeter(grid)
    for x in range(1, len(grid[0]) - 1):
        for y in range(1, len(grid) - 1):
            sight_lines = get_sight_lines(x, y, grid)
            visible += 1 if check_visible(grid[x][y], sight_lines) else 0
    return visible


def calc_scenic_score(height, sight_lines):
    views = []
    for line in [_ for _ in sight_lines if _]:
        for idx, tree in enumerate(line):
            if tree >= height:
                break
        views.append(len(line[: idx + 1]))
    return reduce(lambda x, y: x * y, views)


def process2(data):
    grid = build_grid(data)
    max_scenic_score = 0
    for x in range(1, len(grid[0]) - 1):
        for y in range(1, len(grid) - 1):
            sight_lines = get_sight_lines(y, x, grid)
            tree_scenic_score = calc_scenic_score(grid[y][x], sight_lines)
            if tree_scenic_score > max_scenic_score:
                max_scenic_score = tree_scenic_score
    return max_scenic_score


def get_sight_lines(x, y, grid):
    left = grid[x][:y][::-1]
    right = grid[x][y + 1 :]
    top = [row[y] for row in grid[:x]][::-1]
    bottom = [row[y] for row in grid[x + 1 :]]
    return left, right, top, bottom


def check_visible(height, sight_lines):
    return any([height > max(line) for line in sight_lines if line])


def main(filename):
    file_data = get_data_from_file(filename)
    visible = process(file_data)
    print(f"visible count = {visible}")
    visible = process2(file_data)
    print(f"visible count 2 = {visible}")


if __name__ in "__main__":
    main("day_8.txt")
