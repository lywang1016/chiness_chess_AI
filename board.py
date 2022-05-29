import copy
import numpy as np
from utils import board_turn180, board_to_key, key_to_board
from constant import piece_values

class ChessBoard:
    def __init__(self, record = False):
        self.record = record
        self.board = np.zeros((10, 9))
        self.done = False
        self.win = None
        self.dataset = {}
        self.red_history = []
        self.black_history = []
        self.reset_board()

    def reset_board(self):
        self.board = np.zeros((10, 9))
        self.board[0][0] = piece_values['b_rook']
        self.board[0][1] = piece_values['b_knight']
        self.board[0][2] = piece_values['b_minister']
        self.board[0][3] = piece_values['b_warrior']
        self.board[0][4] = piece_values['b_king']
        self.board[0][5] = piece_values['b_warrior']
        self.board[0][6] = piece_values['b_minister']
        self.board[0][7] = piece_values['b_knight']
        self.board[0][8] = piece_values['b_rook']
        self.board[2][1] = piece_values['b_cannon']
        self.board[2][7] = piece_values['b_cannon']
        self.board[3][0] = piece_values['b_pawn']
        self.board[3][2] = piece_values['b_pawn']
        self.board[3][4] = piece_values['b_pawn']
        self.board[3][6] = piece_values['b_pawn']
        self.board[3][8] = piece_values['b_pawn']
        self.board[6][0] = piece_values['r_pawn']
        self.board[6][2] = piece_values['r_pawn']
        self.board[6][4] = piece_values['r_pawn']
        self.board[6][6] = piece_values['r_pawn']
        self.board[6][8] = piece_values['r_pawn']
        self.board[7][1] = piece_values['r_cannon']
        self.board[7][7] = piece_values['r_cannon']
        self.board[9][0] = piece_values['r_rook']
        self.board[9][1] = piece_values['r_knight']
        self.board[9][2] = piece_values['r_minister']
        self.board[9][3] = piece_values['r_warrior']
        self.board[9][4] = piece_values['r_king']
        self.board[9][5] = piece_values['r_warrior']
        self.board[9][6] = piece_values['r_minister']
        self.board[9][7] = piece_values['r_knight']
        self.board[9][8] = piece_values['r_rook']
        self.done = False
        self.win = None
        self.dataset = {}
        self.red_history = []
        self.black_history = []
        self.dataset = {}

    def set_done(self, win_color):
        self.win = win_color
        self.done = True

    def check_done(self):
        have_rk = False
        have_bk = False
        for i in range(3):
            for j in range(3, 6):
                if self.board[i][j] == piece_values['b_king']:
                    have_bk = True
        for i in range(7, 10):
            for j in range(3, 6):
                if self.board[i][j] == piece_values['r_king']:
                    have_rk = True
        if have_rk and have_bk:
            self.win = None
            self.done = False
        else:
            if have_rk:
                self.win = 'r'
            else:
                self.win = 'b'
            self.done = True

    def load_board(self, board):
        self.board = board
        self.check_done()
    
    def board_states(self):
        return copy.deepcopy(self.board)

    def rotate_board(self):
        self.board = board_turn180(self.board)
    
    def move_piece(self, position, move, color):
        if self.record:
            if color == 'r':
                self.red_history.append(board_to_key(self.board_states()))
            else:
                self.black_history.append(board_to_key(board_turn180(self.board_states())))

        value = self.board[position[0]][position[1]]
        self.board[position[0]][position[1]] = 0
        self.board[position[0]+move[0]][position[1]+move[1]] = value
        self.check_done()

    def fill_dataset(self):
        if self.record:
            if self.win == 'r':
                for key in self.red_history:
                    if key not in self.dataset:
                        self.dataset[key] = [1, 0, 0]
                    else:
                        self.dataset[key][0] += 1
                for key in self.black_history:
                    if key not in self.dataset:
                        self.dataset[key] = [0, 0, 1]
                    else:
                        self.dataset[key][2] += 1
            if self.win == 'b':
                for key in self.black_history:
                    if key not in self.dataset:
                        self.dataset[key] = [1, 0, 0]
                    else:
                        self.dataset[key][0] += 1
                for key in self.red_history:
                    if key not in self.dataset:
                        self.dataset[key] = [0, 0, 1]
                    else:
                        self.dataset[key][2] += 1
            if self.win == 't':
                for key in self.black_history:
                    if key not in self.dataset:
                        self.dataset[key] = [0, 1, 0]
                    else:
                        self.dataset[key][1] += 1
                for key in self.red_history:
                    if key not in self.dataset:
                        self.dataset[key] = [0, 1, 0]
                    else:
                        self.dataset[key][1] += 1
