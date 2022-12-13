from advent_of_code_2022.common import get_data_from_file


def move(direction, hx, hy):
    new_x = hx
    new_y = hy
    if direction == "R":
        new_x = hx + 1
    elif direction == "L":
        new_x = hx - 1
    elif direction == "U":
        new_y = hy + 1
    elif direction == "D":
        new_y = hy - 1
    return new_x, new_y


def move_tail(h_x, h_y, t_x, t_y):
    distance = abs(h_x - t_x) + abs(h_y - t_y)
    if h_x == t_x and distance >= 2:
        return t_x, h_y - 1 if h_y > t_y else h_y + 1
    elif h_y == t_y and distance >= 2:
        return h_x - 1 if h_x > t_x else h_x + 1, t_y
    if distance > 2:
        if h_x > t_x:
            return t_x + 1, t_y + 1 if h_y > t_y else t_y - 1
        if h_x < t_x:
            return t_x - 1, t_y + 1 if h_y > t_y else t_y - 1
    return t_x, t_y


def process(data, knots):
    instructions = parse_instructions(data)
    history = build_history_for_knots(knots)
    execute_instructions(history, instructions, knots)
    return len(set(history[knots]))


def execute_instructions(history, instructions, knots):
    for direction, steps in instructions:
        for _ in range(steps):
            move_head(direction, history)
            for knot in range(1, knots + 1):
                tx, ty = move_tail(*history[knot - 1][-1], *history[knot][-1])
                history[knot].append((tx, ty))


def build_history_for_knots(knots):
    return {i: [(0, 0)] for i in range(knots + 1)}


def move_head(direction, history):
    hx, hy = history[0][-1]
    new_hx, new_hy = move(direction, hx, hy)
    history[0].append((new_hx, new_hy))


def extract_move(line_data):
    direction, number = line_data.split(" ")
    return direction, int(number)


def parse_instructions(data):
    return [extract_move(line) for line in data.split("\n")]


def main(filename, knots):
    file_data = get_data_from_file(filename)
    position = process(file_data, knots)
    print(f"There is {position} position")


if __name__ == "__main__":
    main("day_9.txt", 1)
    main("day_9.txt", 9)
