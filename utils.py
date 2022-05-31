import numpy as np
from constant import values_piece2

def rotate_action(posi, move):
    move_ = (-move[0], -move[1])
    posi_ = (9 - posi[0], 8 - posi[1])
    return posi_, move_

def board_turn180(board_in):
    board = board_in[::-1,::-1]
    for i in range(10):
        for j in range(9):
            board[i][j] = -board[i][j]
    return board

def board_to_key(board):
    key = tuple(map(tuple, board))
    return key

def key_to_board(key):
    board = np.zeros((10, 9))
    for i in range(10):
        for j in range(9):
            board[i][j] = key[i][j]
    return board

def print_dataset(dataset):
    for key in dataset:
        print(dataset[key])
        for i in range(10):
            row_str = ''
            for j in range(9):
                row_str += values_piece2[key[i][j]]
            print(row_str)
        print('##################')

def print_board(board):
    for i in range(10):
        row_str = ''
        for j in range(9):
            row_str += values_piece2[board[i][j]]
        print(row_str)
    print('##################')

def merge_dataset(dataset1, dataset2): # merge dataset2 data into dataset1
    for key in dataset2:
        if key not in dataset1:
            dataset1[key] = dataset2[key]
        else:
            for i in range(3):
                dataset1[key][i] += dataset2[key][i]