import sys

sys.path.insert(0, "../utils/py")
import utils

from collections import Counter


def calculate_single_round_score(round_selection):
    """
    Rock defeats Scissors
    Scissors defeats Paper
    Paper defeats Rock
    If both players choose the same shape, the round instead ends in a draw.

    The score for a single round is the score for the shape you selected (1 for
    Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of
    the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

    A for Rock, B for Paper, and C for Scissors - Elf
    X for Rock, Y for Paper, and Z for Scissors - me

    ('A', 'X'): outcome_of_round = 3, shape_me_selected = 1
    ('A', 'Y'): outcome_of_round = 6, shape_me_selected = 2
    ('A', 'Z'): outcome_of_round = 0, shape_me_selected = 3
    ('B', 'X'): outcome_of_round = 0, shape_me_selected = 1
    ('B', 'Y'): outcome_of_round = 3, shape_me_selected = 2
    ('B', 'Z'): outcome_of_round = 6, shape_me_selected = 3
    ('C', 'X'): outcome_of_round = 6, shape_me_selected = 1
    ('C', 'Y'): outcome_of_round = 0, shape_me_selected = 2
    ('C', 'Z'): outcome_of_round = 3, shape_me_selected = 3

    input: round_selection - ('A','X')
    """
    match round_selection:
        case ("A", "X"):
            outcome_of_round = 3
            shape_me_selected = 1
            return outcome_of_round + shape_me_selected
        case ("A", "Y"):
            outcome_of_round = 6
            shape_me_selected = 2
            return outcome_of_round + shape_me_selected
        case ("A", "Z"):
            outcome_of_round = 0
            shape_me_selected = 3
            return outcome_of_round + shape_me_selected
        case ("B", "X"):
            outcome_of_round = 0
            shape_me_selected = 1
            return outcome_of_round + shape_me_selected
        case ("B", "Y"):
            outcome_of_round = 3
            shape_me_selected = 2
            return outcome_of_round + shape_me_selected
        case ("B", "Z"):
            outcome_of_round = 6
            shape_me_selected = 3
            return outcome_of_round + shape_me_selected
        case ("C", "X"):
            outcome_of_round = 6
            shape_me_selected = 1
            return outcome_of_round + shape_me_selected
        case ("C", "Y"):
            outcome_of_round = 0
            shape_me_selected = 2
            return outcome_of_round + shape_me_selected
        case ("C", "Z"):
            outcome_of_round = 3
            shape_me_selected = 3
            return outcome_of_round + shape_me_selected


def calculate_single_round_score_part2(round_selection):
    """
    Rock defeats Scissors
    Scissors defeats Paper
    Paper defeats Rock. 12772
    If both players choose the same shape, the round instead ends in a draw.

    The score for a single round is the score for the shape you selected (1 for
    Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of
    the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

    A for Rock, B for Paper, and C for Scissors - Elf
    X you lose, Y you draw, and Z you win

    ('A', 'X'): outcome_of_round = 0, shape_me_selected = 3
    ('A', 'Y'): outcome_of_round = 3, shape_me_selected = 1
    ('A', 'Z'): outcome_of_round = 6, shape_me_selected = 2
    ('B', 'X'): outcome_of_round = 0, shape_me_selected = 1
    ('B', 'Y'): outcome_of_round = 3, shape_me_selected = 2
    ('B', 'Z'): outcome_of_round = 6, shape_me_selected = 3
    ('C', 'X'): outcome_of_round = 0, shape_me_selected = 2
    ('C', 'Y'): outcome_of_round = 3, shape_me_selected = 3
    ('C', 'Z'): outcome_of_round = 6, shape_me_selected = 1

    input: round_selection - ('A','X')
    """
    match round_selection:
        case ("A", "X"):
            outcome_of_round = 0
            shape_me_selected = 3
            return outcome_of_round + shape_me_selected
        case ("A", "Y"):
            outcome_of_round = 3
            shape_me_selected = 1
            return outcome_of_round + shape_me_selected
        case ("A", "Z"):
            outcome_of_round = 6
            shape_me_selected = 2
            return outcome_of_round + shape_me_selected
        case ("B", "X"):
            outcome_of_round = 0
            shape_me_selected = 1
            return outcome_of_round + shape_me_selected
        case ("B", "Y"):
            outcome_of_round = 3
            shape_me_selected = 2
            return outcome_of_round + shape_me_selected
        case ("B", "Z"):
            outcome_of_round = 6
            shape_me_selected = 3
            return outcome_of_round + shape_me_selected
        case ("C", "X"):
            outcome_of_round = 0
            shape_me_selected = 2
            return outcome_of_round + shape_me_selected
        case ("C", "Y"):
            outcome_of_round = 3
            shape_me_selected = 3
            return outcome_of_round + shape_me_selected
        case ("C", "Z"):
            outcome_of_round = 6
            shape_me_selected = 1
            return outcome_of_round + shape_me_selected


measure_time = utils.stopwatch()


@measure_time
def parse(raw_data):
    return [(me[0:1], me[2:3]) for me in raw_data.split("\n")]


# PART 1
@measure_time
def solve1(data):
    return sum(
        [calculate_single_round_score(x[0]) * x[1] for x in Counter(data).items()]
    )


# PART 2
@measure_time
def solve2(data):
    return sum(
        [calculate_single_round_score_part2(x[0]) * x[1] for x in Counter(data).items()]
    )


if __name__ == "__main__":
    data = parse(open("input.txt").read().strip())
    print("Part 1: {}".format(solve1(data)))
    print("Part 2: {}".format(solve2(data)))

    print("\nTime taken:")
    for func, time in measure_time.times:
        print(f"{func:8}{time}s")
    print("----------------")
    print("total   {}s".format(sum(t for _, t in measure_time.times)))
