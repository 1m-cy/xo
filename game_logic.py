# game_logic.py

board = [' ' for _ in range(9)]

def check_winner(player):

    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True

    return False

def is_draw():
    return ' ' not in board

def reset_board():

    global board
    board = [' ' for _ in range(9)]