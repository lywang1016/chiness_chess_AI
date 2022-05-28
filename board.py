import copy
import numpy as np
from constant import piece_values

class ChessBoard:
    def __init__(self):
        self.board = np.zeros((10, 9))
        self.done = False
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

    def load_board(self, board):
        self.board = board
    
    def board_states(self):
        return copy.deepcopy(self.board)

    def rotate_board(self):
        self.board = self.board[::-1,::-1]
        for i in range(10):
            for j in range(9):
                self.board[i][j] = -self.board[i][j]
    
    def move_piece(self, position, move):
        value = self.board[position[0]][position[1]]
        self.board[position[0]][position[1]] = 0
        self.board[position[0]+move[0]][position[1]+move[1]] = value
        # check done
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
            self.done = False
        else:
            self.done = True