from collections import defaultdict, deque

from advent_of_code_2022.common import get_data_from_file


def get_crane_status(data):
    stack_rows = data.split("\n")[:-1]
    stacks = defaultdict(deque)
    for row in reversed(stack_rows):
        for idx, val in enumerate(row[1::4], start=1):
            if val.isalpha():
                stacks[idx].append(val)
    return stacks


def get_move_instructions(data):
    inst_lines = data.split("\n")
    instructions = [get_instruction_from_line(line) for line in inst_lines]
    return instructions


def get_instruction_from_line(line):
    return tuple([int(x) for x in line.replace("move", "").replace("from", "").replace("to", "").split()])


def process(data, strategy):
    raw_crane_status, raw_instruction = data.split("\n\n")
    crane_stacks = get_crane_status(raw_crane_status)
    instructions = get_move_instructions(raw_instruction)
    execute_instructions(crane_stacks, instructions, strategy)

    return take_top_of_pile_letters(crane_stacks)


def take_top_of_pile_letters(crane_stacks):
    return "".join([crane_stacks[crane].pop() for crane in crane_stacks])


def execute_instructions(crane_stacks, instructions, strategy):
    for move, _from, _to in instructions:
        strategy(_from, _to, crane_stacks, move)


def part_1_strategy(_from, _to, crane_stacks, move):
    for i in range(move):
        crate = crane_stacks[_from].pop()
        crane_stacks[_to].append(crate)


def part_2_strategy(_from, _to, crane_stacks, move):
    group = []
    for _ in range(move):
        if crane_stacks[_from]:
            crate = crane_stacks[_from].pop()
            group.append(crate)
    crane_stacks[_to].extend(group[::-1])


def main(filename, strategy):
    file_data = get_data_from_file(filename)
    code = process(file_data, strategy)
    print(f"The code is  {code}")


if __name__ in "__main__":
    main("day_5.txt", part_1_strategy)
    main("day_5.txt", part_2_strategy)
