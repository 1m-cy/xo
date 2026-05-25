# ai.py

import math
import random

from game_logic import board, check_winner, is_draw

#  minimax
def minimax(is_maximizing):

    if check_winner('O'):
        return 1

    if check_winner('X'):
        return -1

    if is_draw():
        return 0

    if is_maximizing:

        best_score = -math.inf

        for i in range(9):

            if board[i] == ' ':

                board[i] = 'O'

                score = minimax(False)

                board[i] = ' '

                best_score = max(score, best_score)

        return best_score

    else:

        best_score = math.inf

        for i in range(9):

            if board[i] == ' ':

                board[i] = 'X'

                score = minimax(True)

                board[i] = ' '

                best_score = min(score, best_score)

        return best_score

# حركة عشوائية
def random_move():

    empty_cells = []

    for i in range(9):

        if board[i] == ' ':
            empty_cells.append(i)

    return random.choice(empty_cells)

# أفضل حركة بالذكاء الاصطناعي
def best_move():

    best_score = -math.inf
    move = 0

    for i in range(9):

        if board[i] == ' ':

            board[i] = 'O'

            score = minimax(False)

            board[i] = ' '

            if score > best_score:

                best_score = score
                move = i

    return move

# مستويات الصعوبة
def get_ai_move(difficulty):

    # Easy
    if difficulty == "Easy":
        return random_move()

    # Medium
    elif difficulty == "Medium":

        # 50% ذكي - 50% عشوائي
        if random.random() < 0.5:
            return best_move()
        else:
            return random_move()

    # Hard
    elif difficulty == "Hard":
        return best_move()