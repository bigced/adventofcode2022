from collections import defaultdict

from advent_of_code_2022.common import get_data_from_file


class Monkey:
    def __init__(self, items, operation, test, target):
        self.items = items
        self.operation = operation
        self.test = test
        self.target = target


def parse_input(data):
    monkey_strings = data.split("\n\n")
    monkeys = []
    for monkey_string in monkey_strings:
        monkeys.append(create_monkey_from_string(monkey_string))
    return monkeys


def create_monkey_from_string(monkey_string):
    name, items, operation, test, if_true, if_false = [line.strip() for line in monkey_string.split("\n")]
    items = [int(item.strip()) for item in items[16:].split(",")]
    operation = operation.split("=")[-1].strip()
    test = int(test.split(" ")[-1])
    if_true = int(if_true.split(" ")[-1])
    if_false = int(if_false.split(" ")[-1])
    target = (if_false, if_true)
    monkey = Monkey(items, operation, test, target)
    return monkey


def solve(data, rounds, part):
    monkeys = parse_input(data)

    divisor = 1
    for m in monkeys:
        divisor *= m.test

    monkey_counter = defaultdict(int)
    for _ in range(rounds):
        for i, monkey in enumerate(monkeys):
            while monkey.items:
                increment_monkey_counter(i, monkey_counter)
                move_items_to_monkeys(monkey, monkeys, divisor, part)
    top, second = find_top_2(monkey_counter)
    return top * second


def find_top_2(monkey_counter):
    return sorted(monkey_counter.values(), reverse=True)[:2]


def move_items_to_monkeys(monkey, monkeys, divisor, part):
    old = monkey.items[0]  # noqa
    monkey.items = monkey.items[1:]
    new = eval(monkey.operation)
    if part == 1:
        new //= 3
    else:
        new %= divisor
    test = (new % monkey.test) == 0
    target_monkey = monkey.target[test]
    monkeys[target_monkey].items.append(new)


def increment_monkey_counter(i, monkey_counter):
    monkey_counter[i] += 1


def main(filename, rounds, part):
    file_data = get_data_from_file(filename)
    monkey_business = solve(file_data, rounds, part)
    print(f"There is {monkey_business} monkey business")


if __name__ in "__main__":
    main("day_11.txt", 20, 1)
    main("day_11.txt", 10000, 2)
