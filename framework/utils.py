import numpy as np
import h5py
from os.path import exists
from framework.constant import values_piece2

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
        print('##### Before ######')
        print_board(key_to_board(key[0]))
        print('##### After ######')
        print_board(key_to_board(key[1]))

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

def h5py_to_dataset(x_path, y_path):
    dataset = {}
    if exists(x_path) and exists(y_path):
        fx = h5py.File(x_path, 'r')
        fy = h5py.File(y_path, 'r')
        for key in fx:
            boards = np.array(fx[key])
            data = np.array(fy[key])
            dataset[(board_to_key(boards[0]), board_to_key(boards[1]))] = data
        fx.close()
        fy.close()
    return dataset

def dataset_to_h5py(dataset, x_path, y_path):
    fx = h5py.File(x_path, "w")
    fy = h5py.File(y_path, "w")
    for key in dataset:
        fx.create_dataset(str(key), data=np.array((key_to_board(key[0]), key_to_board(key[1]))))
        fy.create_dataset(str(key), data=dataset[key])
    fx.close()
    fy.close()

def h5py_add_dataset(x_path, y_path, dataset):
    fx = h5py.File(x_path, "a")
    fy = h5py.File(y_path, "a")
    for key in dataset:
        if str(key) in fx:
            data_in_file = np.array(fy[str(key)])
            for i in range(3):
                data_in_file[i] += dataset[key][i]
            del fy[str(key)]
            fy.create_dataset(str(key), data=data_in_file)
        else:
            fx.create_dataset(str(key), data=np.array((key_to_board(key[0]), key_to_board(key[1]))))
            fy.create_dataset(str(key), data=dataset[key])
    fx.close()
    fy.close()
