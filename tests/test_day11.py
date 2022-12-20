from advent_of_code_2022.day_11 import Monkey, parse_input, solve


def test_parse_input_one_monkey():
    data = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3"""
    monkeys = parse_input(data)
    assert len(monkeys) == 1
    monkey = monkeys[0]
    assert isinstance(monkey, Monkey)
    assert monkey.items == [79, 98]
    assert monkey.operation == "old * 19"
    assert monkey.test == 23
    assert monkey.target == (3, 2)


def test_parse_input_two_monkey():
    data = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0"""
    monkeys = parse_input(data)
    assert len(monkeys) == 2
    monkey = monkeys[0]
    assert isinstance(monkey, Monkey)
    assert monkey.items == [79, 98]
    assert monkey.operation == "old * 19"
    assert monkey.test == 23
    assert monkey.target == (3, 2)

    monkey = monkeys[1]
    assert isinstance(monkey, Monkey)
    assert monkey.items == [54, 65, 75, 74]
    assert monkey.operation == "old + 6"
    assert monkey.test == 19
    assert monkey.target == (0, 2)


def test_solve_20_rounds():
    data = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

    monkey_business = solve(data, 20, 1)
    assert monkey_business == 10605


def test_solve_part2():
    data = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

    monkey_business = solve(data, 10000, 2)
    assert monkey_business == 2713310158
