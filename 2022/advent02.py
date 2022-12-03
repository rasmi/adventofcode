"""Day 2: Rock Paper Scissors"""

letter_to_shape = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}

letter_to_outcome = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}

shape_value = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

outcome_value = {
    'win': 6,
    'draw': 3,
    'lose': 0
}

wins = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}
loses = {loser: winner for winner, loser in wins.items()}


def round_score_encrypted(round_):
    """Compute the score of a round based on the encrypted strategy.

    Arguments:
        round_: String of the form 'OPPONENT_LETTER PLAYER_LETTER' where
            OPPONENT_LETTER and PLAYER_LETTER are in {A, B, C, X, Y, Z}

    Returns:
        Score of the round, based on PLAYER's shape value and the outcome of the round.
    """
    opponent_letter, player_letter = round_.split(' ')
    opponent, player = letter_to_shape[opponent_letter], letter_to_shape[player_letter]

    outcome = ''
    if player == opponent:
        outcome = 'draw'
    elif wins[player] == opponent:
        outcome = 'win'
    else:
        outcome = 'lose'

    score = shape_value[player] + outcome_value[outcome]

    return score


def round_score_decrypted(round_):
    """Compute the score of a round based on the decrypted strategy.

    Arguments:
        round_: String of the form 'OPPONENT_LETTER OUTCOME_LETTER' where
            OPPONENT_LETTER is in {A, B, C} and OUTCOME_LETTER is in {X, Y, Z}

    Returns:
        Score of the round, based on PLAYER's shape value and the outcome of the round.
    """
    opponent_letter, outcome_letter = round_.split(' ')
    opponent, outcome = letter_to_shape[opponent_letter], letter_to_outcome[outcome_letter]

    player = ''
    if outcome == 'win':
        player = loses[opponent]
    elif outcome == 'lose':
        player = wins[opponent]
    else:
        player = opponent

    score = shape_value[player] + outcome_value[outcome]

    return score


if __name__ == '__main__':
    with open('input02.txt', 'r', encoding='utf-8') as input_file:
        rounds = input_file.read().splitlines()

    round_scores_encrypted = [round_score_encrypted(round_) for round_ in rounds]
    total_score_encrypted = sum(round_scores_encrypted)
    print(total_score_encrypted)

    round_scores_decrypted = [round_score_decrypted(round_) for round_ in rounds]
    total_score_decrypted = sum(round_scores_decrypted)
    print(total_score_decrypted)
