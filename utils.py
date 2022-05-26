import numpy as np

piece_values = {
    'b_rook': -1,
    'b_knight': -2,
    'b_cannon': -3,
    'b_minister': -4,
    'b_warrior': -5,
    'b_pawn': -6,
    'b_king': -7,

    'r_rook': 1,
    'r_knight': 2,
    'r_cannon': 3,
    'r_minister': 4,
    'r_warrior': 5,
    'r_pawn': 6,
    'r_king': 7
}

values_piece = {
    -1: 'b_rook',
    -2: 'b_knight',
    -3: 'b_cannon',
    -4: 'b_minister',
    -5: 'b_warrior',
    -6: 'b_pawn',
    -7: 'b_king',

    1: 'r_rook',
    2: 'r_knight',
    3: 'r_cannon',
    4: 'r_minister',
    5: 'r_warrior',
    6: 'r_pawn',
    7: 'r_king'
}

class ChessBoard:
    def __init__(self):
        self.board = np.zeros((10, 9))
        self.reset_board()

    def reset_board(self):
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
    
    def board_states(self):
        return self.board

class Piece:
    def __init__(self, name, color, position):
        self.name = name
        self.color = color
        self.row = position[0]
        self.col = position[1]
    
    def next_valid_move():
        return 

class King(Piece):
    def __init__(self, color, position):
        self.name = 'king'
        self.color = color
        self.value = piece_values[self.color + '_' + self.name]
        self.row = position[0]
        self.col = position[1]
        self.j_max = 5
        self.j_min = 3
        if self.color == 'r':
            self.i_max = 9
            self.i_min = 7
        else:
            self.i_max = 2
            self.i_min = 0

    def next_valid_move(self, board):
        res = []
        if self.row+1 <= self.i_max:    #able to move down
            if board[self.row+1][self.col] * self.value <= 0:
                res.append((1, 0))
        if self.row-1 >= self.i_min:    #able to move up
            if board[self.row-1][self.col] * self.value <= 0:
                res.append((-1, 0))
        if self.col+1 <= self.j_max:    #able to move right
            if board[self.row][self.col+1] * self.value <= 0:
                hide_flag = False
                if self.row > 5:    # red
                    for i in range(self.row-1, -1, -1):
                        if board[i][self.col+1] != 0 and board[i][self.col+1] != -self.value:   #some thing there
                            hide_flag = True
                            break
                else:               # black
                    for i in range(self.row+1, 10):
                        if board[i][self.col+1] != 0 and board[i][self.col+1] != -self.value:   #some thing there
                            hide_flag = True
                            break
                if hide_flag:
                    res.append((0, 1))
        if self.col-1 >= self.j_min:    #able to move left
            if board[self.row][self.col-1] * self.value <= 0:
                hide_flag = False
                if self.row > 5:    # red
                    for i in range(self.row-1, 0, -1):
                        if board[i][self.col-1] != 0 and board[i][self.col-1] != -self.value:   #some thing there
                            hide_flag = True
                            break
                else:               # black
                    for i in range(self.row+1, 10):
                        if board[i][self.col-1] != 0 and board[i][self.col-1] != -self.value:   #some thing there
                            hide_flag = True
                            break
                if hide_flag:
                    res.append((0, -1))
        return res