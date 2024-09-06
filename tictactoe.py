"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
   X_count = sum(row.count('X') for row in board)
   O_count = sum(row.count('O') for row in board)
   return 'X' if X_count == O_count else 'O'


def actions(board):
    return{(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}


def result(board, action):
    if board[action[0]][action[1]] != EMPTY:
        raise Exception("Invalid move")
    new_board = [row[:] for row in board]
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    for player in ['X', 'O']:
        #checks the rows, columns, and diagonals
        if any(all(cell == player for cell in row) for row in board):
            return player
        if any(all(board[i][j] == player for i in range(3)) for j in range(3)):
            return player
        if all(board[i][i] == player for i in range (3)) or all(board[i][2-i] == player for i in range(3)):
            return player
        return None


def terminal(board):
    return winner(board) is not None or all(cell != EMPTY for row in board for cell in row)


def utility(board):
    win = winner(board)
    if win == 'X':
        return 1
    elif win == 'O':
        return -1
    return 0


def minimax(board):
    if terminal(board):
        return None
    
    current_player = player(board)

    if current_player == 'X':
        #Maximize the score for 'X'
        best_value = -float('inf')
        best_move = None
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_move = action
        return best_move
    else:
        #Minimize the score for 'O'
        best_value = float('inf')
        best_move = None
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value 
                best_move = action
            return best_move

def max_value(board):
    if terminal(board):
        return utility(board)
    value = -float('inf')
    for action in actions(board):
        value = max(value, min_value(result(board, action)))
    return value

def min_value(board):
    if terminal(board):
        return utility(board)
    value = float('inf')
    for action in actions(board):
        value = min(value, max_value(result(board, action)))
        return value