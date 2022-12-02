from advent_of_code_2022.common import get_data_from_file


def get_elf_data_from_file_data(file_data):
    return file_data.split("\n\n")


def calculate_elf_calorie(elf_data):
    return sum([int(x.strip()) for x in elf_data.split("\n")])


def get_max_calorie(elf_data):
    return max(convert_elf_data_to_list(elf_data))


def convert_elf_data_to_list(elf_data):
    return [calculate_elf_calorie(x) for x in elf_data]


def get_max_3_calorie(elf_data):
    list_of_elf_data = convert_elf_data_to_list(elf_data)
    list_of_elf_data.sort()
    return sum(list_of_elf_data[-3:])


def main(filename):
    file_data = get_data_from_file(filename)
    elf_data = get_elf_data_from_file_data(file_data)
    max_calorie = get_max_calorie(elf_data)
    three_elves_calories = get_max_3_calorie(elf_data)
    print(f"The max calorie is {max_calorie} and 3 elves is {three_elves_calories}")


if __name__ in "__main__":
    main("day_1.txt")
