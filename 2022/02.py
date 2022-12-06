from aocd.models import Puzzle
from aocd.transforms import lines
from enum import Enum

# Input
puzzle = Puzzle(year=2022, day=2)
encrypted_rps_strategy_guide = lines(puzzle.input_data)


# Solution
class RPSChoice(Enum):
    # Hacky way to encode winning/losing choices by predefining strings
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def __init__(self, choice_score):
        self.choice_score = choice_score

    @classmethod
    def get_rps_choice(cls, encrypted_choice):
        rock_choice = 'A'
        paper_choice = 'B'

        if encrypted_choice == rock_choice:
            return cls.ROCK
        elif encrypted_choice == paper_choice:
            return cls.PAPER
        else:
            # Assume it is 'C'
            return cls.SCISSORS

    @property
    def winning_option(self):
        if self == self.ROCK:
            return self.SCISSORS
        elif self == self.PAPER:
            return self.ROCK
        else:
            return self.PAPER

    @property
    def losing_option(self):
        if self == self.ROCK:
            return self.PAPER
        elif self == self.PAPER:
            return self.SCISSORS
        else:
            return self.ROCK


class RPSOutcome(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6

    def __init__(self, outcome_score):
        self.outcome_score = outcome_score


# Answer A
def get_score_part_a(opponent_choice, player_choice):
    outcome = RPSOutcome.LOSS
    if opponent_choice == player_choice:
        outcome = RPSOutcome.DRAW
    elif opponent_choice == player_choice.winning_option:
        outcome = RPSOutcome.WIN

    return player_choice.choice_score + outcome.outcome_score


total_score_part_a = 0
part_a_conversion = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}
for rps_game in encrypted_rps_strategy_guide:
    enc_opponent_choice, enc_player_choice = rps_game.split()

    opponent_rps_choice = RPSChoice.get_rps_choice(enc_opponent_choice)
    player_rps_choice = RPSChoice.get_rps_choice(
        part_a_conversion.get(enc_player_choice)
    )

    score = get_score_part_a(opponent_rps_choice, player_rps_choice)
    total_score_part_a += score

puzzle.answer_a = total_score_part_a


# Answer B
def get_score_part_b(opponent_choice, desired_outcome):
    player_choice = opponent_choice
    if desired_outcome == RPSOutcome.WIN:
        player_choice = opponent_choice.losing_option
    elif desired_outcome == RPSOutcome.LOSS:
        player_choice = opponent_choice.winning_option

    return player_choice.choice_score + desired_outcome.outcome_score


total_score_part_b = 0
part_b_conversion = {
    'X': RPSOutcome.LOSS,
    'Y': RPSOutcome.DRAW,
    'Z': RPSOutcome.WIN
}
for rps_game in encrypted_rps_strategy_guide:
    enc_opponent_choice, enc_desired_outcome = rps_game.split()

    opponent_rps_choice = RPSChoice.get_rps_choice(enc_opponent_choice)
    player_desired_outcome = part_b_conversion.get(enc_desired_outcome)

    score = get_score_part_b(opponent_rps_choice, player_desired_outcome)
    total_score_part_b += score

puzzle.answer_b = total_score_part_b
