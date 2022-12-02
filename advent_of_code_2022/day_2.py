from advent_of_code_2022.common import get_data_from_file


def calculate_move_score(me):
    # (1 for Rock, 2 for Paper, and 3 for Scissors)
    score = {"X": 1, "Y": 2, "Z": 3}
    return score.get(me)


def is_winning(me, opponnent):
    winning_data = {
        "rock": "scissor",
        "paper": "rock",
        "scissor": "paper",
    }
    return winning_data.get(me) == opponnent


def calculate_winning_score(opponent, me):
    opponent_converted_value = {"A": "rock", "B": "paper", "C": "scissor"}.get(opponent)
    me_converted_value = {"X": "rock", "Y": "paper", "Z": "scissor"}.get(me)

    if is_tied_score(me_converted_value, opponent_converted_value):
        return 3
    return 6 if is_winning(me_converted_value, opponent_converted_value) else 0


def is_tied_score(me_converted_value, opponent_converted_value):
    return opponent_converted_value == me_converted_value


def game_score(game_data):
    opponent, me = game_data.split(" ")
    my_score = calculate_move_score(me)
    winning_score = calculate_winning_score(opponent, me)
    return my_score + winning_score


def get_total_score(games_data):
    list_of_game_data = games_data.split("\n")
    results = [game_score(x) for x in list_of_game_data]

    return sum(results)


def main(filename):
    file_data = get_data_from_file(filename)
    score = get_total_score(file_data)

    print(f"The total score is {score}")


if __name__ in "__main__":
    main("day_2.txt")
