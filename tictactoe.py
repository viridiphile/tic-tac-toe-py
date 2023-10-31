"""
Tic Tac Toe Player
"""

import copy
import math
global count_o, count_x

X = "X"
O = "O"
EMPTY = None
count_o = 0
count_x = 0


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_o = 0
    count_x = 0
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == X:
                count_x += 1
            if board[i][j] == O:
                count_o += 1
    
    if count_o > count_x:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.append((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise None
    
    i, j = action

    board_copy = copy.deepcopy(board)
    board_copy[i][j] = player(board)

    return board_copy

def row(board, player):
    for i in range(len(board)):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    return False

def column(board, player):
    for j in range(len(board)):
        if board[0][j] == player and board[1][j] == player and board[2][j] == player:
            return True
    return False

def mainDiag(board, player):
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i == j and board[i][j] == player:
                count += 1
    if count == 3:
        return True
    return False

def secondaryDiag(board, player):
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (len(board) - i - 1) == j and board[i][j] == player:
                count += 1
    if count == 3:
        return True
    return False

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if row(board, X) or column(board, X) or mainDiag(board, X) or secondaryDiag(board, X):
        return X
    if row(board, O) or column(board, O) or mainDiag(board, O) or secondaryDiag(board, O):
        return O
    else: 
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    result = winner(board)
    if result is not None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def max_val(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_val(result(board, action)))
    return v
        
def min_val(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_val(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    best_action = None
    best_value = -math.inf if player(board) == X else math.inf

    for action in actions(board):
        value = min_val(result(board, action)) if player(board) == X else max_val(result(board, action))

        if player(board) == X and value > best_value:
            best_value = value
            best_action = action
        elif player(board) == O and value < best_value:
            best_value = value
            best_action = action

    return best_action
