from unittest import mock

from advent_of_code_2022.day_12 import calculate_steps_from_file


@mock.patch("advent_of_code_2022.day_12.get_area_data_from_file")
def test_process(mocked_get_area_data_from_file):
    calculate_steps_from_file("input.txt")
    mocked_get_area_data_from_file.assert_called_once_with("input.txt")
