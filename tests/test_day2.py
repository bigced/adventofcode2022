from unittest import mock

from advent_of_code_2022.day_2 import get_total_score, is_winning, main, part_1_translation, part_2_translation


def test_game_score():
    games_data = """A Y
B X
C Z"""
    total_score = get_total_score(games_data, part_1_translation)

    assert total_score == 15

    total_score = get_total_score(games_data, part_2_translation)

    assert total_score == 12


def test_winning():
    assert is_winning("rock", "paper") is False
    assert is_winning("rock", "scissor") is True


@mock.patch("builtins.print")
@mock.patch("advent_of_code_2022.day_2.get_total_score")
@mock.patch("advent_of_code_2022.day_2.get_data_from_file")
def test_main(
    mocked_get_data_from_file,
    mocked_get_total_score,
    mocked_print,
):

    data = [0, 1, 2, 3]
    joined_raw_data = "\n".join([str(_) for _ in data])
    mocked_get_data_from_file.return_value = joined_raw_data
    mocked_get_total_score.return_value = "SCORE"
    main("filename.txt", part_1_translation)
    mocked_get_data_from_file.assert_called_once_with("filename.txt")
    mocked_get_total_score.assert_called_once_with(joined_raw_data, part_1_translation)
    mocked_print.assert_called_once_with("The total score is SCORE")


def test_part_2_translation():
    assert part_2_translation("Y", "rock") == "rock"
    assert part_2_translation("X", "paper") == "rock"
    assert part_2_translation("Z", "scissor") == "rock"
