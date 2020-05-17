import numpy as np
import random
from time import sleep

def create_board():
    return (np.array([[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]))


# Check for empty places on board
def possibilities(board):
    l = []

    for i in range(len(board)):
        for j in range(len(board)):

            if board[i][j] == 0:
                l.append((i, j))
    return (l)


# Select a random place for the player
# ls=[(0,0),(0,1),(1,1),(0,2),(2,2),(1,0),(1,2),(2,0),(2,1)]
def random_place(board, player):

    selection = possibilities(board)
    current_loc = random.choice(selection)
    board[current_loc] = player
    return (board)
    # board[ls[ct]]=player
    # return (board)

def row_win(board, player):
    for x in range(len(board)):
        win = True

        for y in range(len(board)):
            if board[x, y] != player:
                win = False
                continue

        if win == True:
            return (win)
    return (win)

def col_win(board, player):
    for x in range(len(board)):
        win = True

        for y in range(len(board)):
            if board[y][x] != player:
                win = False
                continue

        if win == True:
            return (win)
    return (win)

# of their marks in a diagonal row
def diag_win(board, player):
    win1 = True
    y = 0
    for x in range(len(board)):
        if board[x, x] != player:
            win1 = False
    win2 = True
    for x in range(len(board)):
        y = len(board) - 1 - x
        if board[x, y] != player:
            win2 = False
    return win1 | win2

def evaluate(board):
    winner = 0

    for player in [1, 2]:
        if (row_win(board, player) or
                col_win(board, player) or
                diag_win(board, player)):
            winner = player

    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner


# Main function to start the game
def play_game():
    board, winner, counter = create_board(), 0, 1
    print(board)
    sleep(2)
    ct=0
    while winner == 0:
        for player in [1, 2]:
            board = random_place(board, player)
            ct=ct+1
            print("Board after " + str(counter) + " move")
            print(board)
            sleep(2)
            counter += 1
            winner = evaluate(board)
            if winner != 0:
                break
    return (winner)


# Driver Code
print("Winner is: " + str(play_game()))
