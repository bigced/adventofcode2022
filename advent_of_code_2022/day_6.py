from collections import Counter

from advent_of_code_2022.common import get_data_from_file


def process(data, start_packet_length):
    for end in range(start_packet_length, len(data)):
        start = end - start_packet_length
        number_of_letters = Counter(data[start:end])
        if are_all_characters_unique(number_of_letters):
            return end


def are_all_characters_unique(number_of_letters):
    return max(number_of_letters.values()) == 1


def main(filename, start_packet_length):
    file_data = get_data_from_file(filename)
    index = process(file_data, start_packet_length)
    print(f"Index is {index}")


if __name__ in "__main__":
    main("day_6.txt", 4)
    main("day_6.txt", 14)
