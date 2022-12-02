from unittest import mock

from advent_of_code_2022.day_1 import (
    calculate_elf_calorie,
    get_elf_data_from_file_data,
    get_max_3_calorie,
    get_max_calorie,
    main,
)


@mock.patch("builtins.print")
@mock.patch("advent_of_code_2022.day_1.get_max_3_calorie")
@mock.patch("advent_of_code_2022.day_1.get_max_calorie")
@mock.patch("advent_of_code_2022.day_1.get_elf_data_from_file_data")
@mock.patch("advent_of_code_2022.day_1.get_data_from_file")
def test_main(
    mocked_get_data_from_file,
    mocked_get_elf_data_from_file_data,
    mocked_get_max_calorie,
    mocked_get_max_3_calorie,
    mocked_print,
):
    data = [0, 1, 2, 3]
    joined_raw_data = "\n".join([str(_) for _ in data])
    mocked_get_data_from_file.return_value = joined_raw_data
    mocked_get_elf_data_from_file_data.return_value = data
    mocked_get_max_calorie.return_value = 24000
    mocked_get_max_3_calorie.return_value = 45000
    main("filename.txt")
    mocked_get_data_from_file.assert_called_once_with("filename.txt")
    mocked_get_elf_data_from_file_data.assert_called_once_with(joined_raw_data)
    mocked_get_max_calorie.assert_called_once_with(data)
    mocked_get_max_3_calorie.assert_called_once_with(data)
    mocked_print.assert_called_once_with("The max calorie is 24000 and 3 elves is 45000")


def test_data_from_file():
    file_data = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
    elf_data = get_elf_data_from_file_data(file_data)

    assert len(elf_data) == 5
    assert calculate_elf_calorie(elf_data[0]) == 6000
    assert calculate_elf_calorie(elf_data[1]) == 4000
    assert calculate_elf_calorie(elf_data[2]) == 11000
    assert calculate_elf_calorie(elf_data[3]) == 24000
    assert calculate_elf_calorie(elf_data[4]) == 10000

    assert get_max_calorie(elf_data) == 24000

    assert get_max_3_calorie(elf_data) == 45000
