from advent_of_code_2022.common import get_data_from_file


def process(data, width):
    cycles = run_operations(data)

    for i, x in enumerate(cycles):
        if i % width == 20:
            print(i, x)
    signal_strength = sum([i * x for i, x in enumerate(cycles) if i % width == 20])
    return signal_strength


def run_operations(data):
    x = 1
    cycles = [1]
    for instruction in data.split("\n"):
        cycles, x = process_instruction(cycles, x, instruction)
    return cycles


def process_instruction(cycles, x, instruction):
    cycles.append(x)
    if instruction != "noop":
        cycles.append(x)
        x += int(instruction.split(" ")[-1])
    return cycles, x


def main(filename, width):
    file_data = get_data_from_file(filename)
    position = process(file_data, width)
    print(f"There is {position} position")


def is_end_of_line(i, width):
    return (i + 1) % width == 0


def process2(file_data, width):
    rows = []
    row_string = ""
    for i, x in enumerate(run_operations(file_data)[1:]):
        row_string += draw_sprite(i, width, x)
        if is_end_of_line(i, width):
            row_string = save_string_and_reset_row(row_string, rows)
    return rows


def save_string_and_reset_row(row_string, rows):
    rows.append(row_string)
    row_string = ""
    return row_string


def draw_sprite(cycle_number, width, x):
    return ".#"[abs(cycle_number % width - x) < 2]


def main2(filename, width):
    file_data = get_data_from_file(filename)
    rows = process2(file_data, width)
    for row in rows:
        print(row)


if __name__ == "__main__":
    main("day_10.txt", 40)
    main2("day_10.txt", 40)
