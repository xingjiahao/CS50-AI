"""
Tic Tac Toe Player
"""

import math
import copy

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
    """
    Returns player who has the next turn on a board.
    """
    num=0
    for row in board:
        num+=row.count(EMPTY)
    if num%2:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    s=set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] is EMPTY:
                s.add((i,j))
    return s


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board=copy.deepcopy(board)
    i,j=action
    if board[i][j]!=EMPTY:
        raise Exception("invalid action")
    new_board[i][j]=player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[0][i]!=EMPTY and (board[0][i]==board[1][i]==board[2][i]):
            return board[0][i]
        if board[i][0]!=EMPTY and (board[i][0]==board[i][1]==board[i][2]):
            return board[i][0]
    if board[0][0]!=EMPTY and board[0][0]==board[1][1]==board[2][2]:
        return board[0][0]
    if board[0][2]!=EMPTY and board[0][2]==board[1][1]==board[2][0]:
        return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win=winner(board)
    if win==X:
        return 1
    elif win==O:
        return -1
    else:
        return 0


def scord(board):
    if terminal(board):
        return utility(board)
    res=[]
    if player(board)==X:
        for act in actions(board):
            sc=scord(result(board,act))
            res.append(sc)
        return max(res)
    else:
        for act in actions(board):
            sc=scord(result(board,act))
            res.append(sc)
        return min(res)


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    cur_palyer=player(board)
    if cur_palyer==X:
        res=[]
        for act in actions(board):
            new_board=result(board,act)
            sc=scord(new_board)
            res.append((sc,act))
        max_res=res[0]
        for sc,act in enumerate(res):
            if sc>max_res[0]:
                max_res=(sc,act)
        return max_res[1]
    else:
        res=[]
        for act in actions(board):
            new_board=result(board,act)
            sc=scord(new_board)
            res.append((sc,act))
        min_res=res[0]
        for sc,act in enumerate(res):
            if sc<min_res[0]:
                min_res=(sc,act)
        return min_res[1]

