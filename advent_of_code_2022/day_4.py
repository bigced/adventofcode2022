from advent_of_code_2022.common import get_data_from_file


def find_overlaps(data, strategy):
    nb_of_pairs = find_overlapped_nb_of_pairs(generate_pairs_from_data(data), strategy)
    return nb_of_pairs


def find_overlapped_nb_of_pairs(pairs, strategy):
    nb_of_pairs = 0
    for pair in pairs:
        intersect = set(pair[0]).intersection(pair[1])
        if strategy(intersect, pair):
            nb_of_pairs += 1
    return nb_of_pairs


def part_1_strategy(intersect, pair):
    return intersect and (len(intersect) == len(pair[1]) or len(intersect) == len(pair[0]))


def part_2_strategy(intersect, pair):
    return len(intersect) > 0


def generate_pairs_from_data(data):
    pairs = []
    for line in data.split("\n"):
        raw_range_1, raw_range_2 = extract_ranges_information(line)
        pairs.append((build_pair_range(raw_range_1), build_pair_range(raw_range_2)))
    return pairs


def extract_ranges_information(line):
    line_pair = line.split(",")
    raw_range_1 = line_pair[0].split("-")
    raw_range_2 = line_pair[1].split("-")
    return raw_range_1, raw_range_2


def build_pair_range(raw_range_1):
    return range(int(raw_range_1[0]), int(raw_range_1[1]) + 1)


def main(filename, strategy):
    file_data = get_data_from_file(filename)
    score = find_overlaps(file_data, strategy)

    print(f"The sum of pairs is {score}")


if __name__ in "__main__":
    main("day_4.txt", part_1_strategy)
    main("day_4.txt", part_2_strategy)
