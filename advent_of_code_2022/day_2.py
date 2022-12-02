from advent_of_code_2022.common import get_data_from_file


def calculate_move_score(me):

    score = {"rock": 1, "paper": 2, "scissor": 3}
    return score.get(me)


def is_winning(me, opponnent):
    winning_data = {
        "rock": "scissor",
        "paper": "rock",
        "scissor": "paper",
    }
    return winning_data.get(me) == opponnent


def calculate_winning_score(opponent, me):

    if is_tied_score(me, opponent):
        return 3
    return 6 if is_winning(me, opponent) else 0


def part_1_translation(me, opponent):
    me_converted_value = {"X": "rock", "Y": "paper", "Z": "scissor"}.get(me)
    return me_converted_value


def part_2_translation(me, opponent):
    winning_data = {
        "rock": "scissor",
        "paper": "rock",
        "scissor": "paper",
    }
    loosing_data = dict([(v, k) for k, v in winning_data.items()])
    if me == "Y":
        return opponent

    return winning_data[opponent] if me == "X" else loosing_data[opponent]


def is_tied_score(me_converted_value, opponent_converted_value):
    return opponent_converted_value == me_converted_value


def game_score(game_data, translator):
    opponent, me = game_data.split(" ")
    opponent_converted_value = {"A": "rock", "B": "paper", "C": "scissor"}.get(opponent)
    me_converted_value = translator(me, opponent_converted_value)
    my_score = calculate_move_score(me_converted_value)
    winning_score = calculate_winning_score(opponent_converted_value, me_converted_value)
    return my_score + winning_score


def get_total_score(games_data, translator):
    list_of_game_data = games_data.split("\n")
    results = [game_score(x, translator) for x in list_of_game_data]

    return sum(results)


def main(filename, translator):
    file_data = get_data_from_file(filename)
    score = get_total_score(file_data, translator)

    print(f"The total score is {score}")


if __name__ in "__main__":
    main("day_2.txt", part_1_translation)
    main("day_2.txt", part_2_translation)
