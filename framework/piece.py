import copy
from framework.constant import piece_values

class Piece:
    def __init__(self, name, color, position):
        self.name = name
        self.color = color
        self.row = position[0]
        self.col = position[1]
    
    def king_valid(self, board, position, move):
        temp = copy.deepcopy(board)
        value = temp[position[0]][position[1]]
        temp[position[0]][position[1]] = 0
        temp[position[0]+move[0]][position[1]+move[1]] = value

        have_rk = False
        have_bk = False
        for i in range(3):
            for j in range(3, 6):
                if temp[i][j] == piece_values['b_king']:
                    bk_posi = (i,j)
                    have_bk = True
        for i in range(7, 10):
            for j in range(3, 6):
                if temp[i][j] == piece_values['r_king']:
                    rk_posi = (i,j)
                    have_rk = True

        if have_rk and have_bk:
            if bk_posi[1] == rk_posi[1]:
                flag = False
                for row in range(bk_posi[0]+1, rk_posi[0]):
                    if temp[row][rk_posi[1]] != 0:
                        flag = True
                        break
                return flag
            else:
                return True
        else:
            return True

class King(Piece):      # Jiang
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
                if self.king_valid(board, (self.row, self.col), (1, 0)):
                    res.append((1, 0))
        if self.row-1 >= self.i_min:    #able to move up
            if board[self.row-1][self.col] * self.value <= 0:
                if self.king_valid(board, (self.row, self.col), (-1, 0)):
                    res.append((-1, 0))
        if self.col+1 <= self.j_max:    #able to move right
            if board[self.row][self.col+1] * self.value <= 0:
                if self.king_valid(board, (self.row, self.col), (0, 1)):
                    res.append((0, 1))
        if self.col-1 >= self.j_min:    #able to move left
            if board[self.row][self.col-1] * self.value <= 0:
                if self.king_valid(board, (self.row, self.col), (0, -1)):
                    res.append((0, -1))
        return res

class Warrior(Piece):      # Shi
    def __init__(self, color, position):
        self.name = 'warrior'
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
        if self.row+1 <= self.i_max and self.col-1 >= self.j_min:    #able to move down left
            if board[self.row+1][self.col-1] * self.value <= 0:
                if self.king_valid(board, (self.row, self.col), (1, -1)):
                    res.append((1, -1))
        if self.row-1 >= self.i_min and self.col-1 >= self.j_min:    #able to move up left
            if board[self.row-1][self.col-1] * self.value <= 0:
                if self.king_valid(board, (self.row, self.col), (-1, -1)):
                    res.append((-1, -1))
        if self.row+1 <= self.i_max and self.col+1 <= self.j_max:    #able to move down right
            if board[self.row+1][self.col+1] * self.value <= 0:
                if self.king_valid(board, (self.row, self.col), (1, 1)):
                    res.append((1, 1))
        if self.row-1 >= self.i_min and self.col+1 <= self.j_max:    #able to move up right
            if board[self.row-1][self.col+1] * self.value <= 0:
                if self.king_valid(board, (self.row, self.col), (-1, 1)):
                    res.append((-1, 1))
        return res

class Minister(Piece):  # Xiang
    def __init__(self, color, position):
        self.name = 'minister'
        self.color = color
        self.value = piece_values[self.color + '_' + self.name]
        self.row = position[0]
        self.col = position[1]
        self.j_max = 8
        self.j_min = 0
        if self.color == 'r':
            self.i_max = 9
            self.i_min = 5
        else:
            self.i_max = 4
            self.i_min = 0

    def next_valid_move(self, board):
        res = []
        if self.row+2 <= self.i_max and self.col-2 >= self.j_min:    #able to move down left
            if board[self.row+2][self.col-2] * self.value <= 0:
                if board[self.row+1][self.col-1] == 0:
                    if self.king_valid(board, (self.row, self.col), (2, -2)):
                        res.append((2, -2))
        if self.row-2 >= self.i_min and self.col-2 >= self.j_min:    #able to move up left
            if board[self.row-2][self.col-2] * self.value <= 0:
                if board[self.row-1][self.col-1] == 0:
                    if self.king_valid(board, (self.row, self.col), (-2, -2)):
                        res.append((-2, -2))
        if self.row+2 <= self.i_max and self.col+2 <= self.j_max:    #able to move down right
            if board[self.row+2][self.col+2] * self.value <= 0:
                if board[self.row+1][self.col+1] == 0:
                    if self.king_valid(board, (self.row, self.col), (2, 2)):
                        res.append((2, 2))
        if self.row-2 >= self.i_min and self.col+2 <= self.j_max:    #able to move up right
            if board[self.row-2][self.col+2] * self.value <= 0:
                if board[self.row-1][self.col+1] == 0:
                    if self.king_valid(board, (self.row, self.col), (-2, 2)):
                        res.append((-2, 2))
        return res

class Rook(Piece):      # ju
    def __init__(self, color, position):
        self.name = 'rook'
        self.color = color
        self.value = piece_values[self.color + '_' + self.name]
        self.row = position[0]
        self.col = position[1]
        self.j_max = 8
        self.j_min = 0
        self.i_max = 9
        self.i_min = 0

    def next_valid_move(self, board):
        res = []
        for row in range(1, self.i_max-self.row+1): #Move down
            if board[self.row+row][self.col] == 0:
                res.append((row, 0))
            else:
                if board[self.row+row][self.col] * self.value < 0:
                    res.append((row, 0))
                break
        for row in range(-1, self.i_min-self.row-1, -1): #Move up
            if board[self.row+row][self.col] == 0:
                res.append((row, 0))
            else:
                if board[self.row+row][self.col] * self.value < 0:
                    res.append((row, 0))
                break
        for col in range(1, self.j_max-self.col+1): #Move right
            if self.king_valid(board, (self.row, self.col), (0, 1)):
                if board[self.row][self.col+col] == 0:
                    res.append((0, col))
                else:
                    if board[self.row][self.col+col] * self.value < 0:
                        res.append((0, col))
                    break
        for col in range(-1, self.j_min-self.col-1, -1): #Move left
            if self.king_valid(board, (self.row, self.col), (0, -1)):
                if board[self.row][self.col+col] == 0:
                    res.append((0, col))
                else:
                    if board[self.row][self.col+col] * self.value < 0:
                        res.append((0, col))
                    break
        return res

class Cannon(Piece):      # pao
    def __init__(self, color, position):
        self.name = 'cannon'
        self.color = color
        self.value = piece_values[self.color + '_' + self.name]
        self.row = position[0]
        self.col = position[1]
        self.j_max = 8
        self.j_min = 0
        self.i_max = 9
        self.i_min = 0

    def next_valid_move(self, board):
        res = []
        flag = False
        for row in range(1, self.i_max-self.row+1): #Move down
            if not flag:
                if board[self.row+row][self.col] == 0:
                    res.append((row, 0))
                else:
                    flag = True
            else:
                if board[self.row+row][self.col] != 0:
                    if board[self.row+row][self.col] * self.value < 0:
                        if self.king_valid(board, (self.row, self.col), (row, 0)):
                            res.append((row, 0))
                    break
        flag = False
        for row in range(-1, self.i_min-self.row-1, -1): #Move up
            if not flag:
                if board[self.row+row][self.col] == 0:
                    res.append((row, 0))
                else:
                    flag = True
            else:
                if board[self.row+row][self.col] != 0:
                    if board[self.row+row][self.col] * self.value < 0:
                        if self.king_valid(board, (self.row, self.col), (row, 0)):
                            res.append((row, 0))
                    break
        flag = False
        for col in range(1, self.j_max-self.col+1): #Move right
            if self.king_valid(board, (self.row, self.col), (0, 1)):
                if not flag:
                    if board[self.row][self.col+col] == 0:
                        res.append((0, col))
                    else:
                        flag = True
                else:
                    if board[self.row][self.col+col] != 0:
                        if board[self.row][self.col+col] * self.value < 0:
                            res.append((0, col))
                        break
        flag = False
        for col in range(-1, self.j_min-self.col-1, -1): #Move left
            if self.king_valid(board, (self.row, self.col), (0, -1)):
                if not flag:
                    if board[self.row][self.col+col] == 0:
                        res.append((0, col))
                    else:
                        flag = True
                else:
                    if board[self.row][self.col+col] != 0:
                        if board[self.row][self.col+col] * self.value < 0:
                            res.append((0, col))
                        break
        return res

class Pawn(Piece):      # bing
    def __init__(self, color, position):
        self.name = 'pawn'
        self.color = color
        self.value = piece_values[self.color + '_' + self.name]
        self.row = position[0]
        self.col = position[1]
        self.j_max = 8
        self.j_min = 0
        if self.color == 'r':
            self.i_max = 6
            self.i_min = 0
        else:
            self.i_max = 9
            self.i_min = 3

    def next_valid_move(self, board):
        res = []
        if self.color == 'r':
            if self.row > 4:    #behind river - move up only
                if board[self.row-1][self.col] * self.value <= 0:
                    res.append((-1, 0))
            else:               # over river- move up and side
                if self.row-1 >= self.i_min:    #able to move up
                    if board[self.row-1][self.col] * self.value <= 0:
                        res.append((-1, 0))
                if self.col+1 <= self.j_max:    #able to move right
                    if board[self.row][self.col+1] * self.value <= 0:
                        if self.king_valid(board, (self.row, self.col), (0, 1)):
                            res.append((0, 1))
                if self.col-1 >= self.j_min:    #able to move left
                    if board[self.row][self.col-1] * self.value <= 0:
                        if self.king_valid(board, (self.row, self.col), (0, -1)):
                            res.append((0, -1))
        else:
            if self.row < 5:    #behind river - move down only
                if board[self.row+1][self.col] * self.value <= 0:
                    res.append((1, 0))
            else:               # over river- move down and side
                if self.row+1 <= self.i_max:    #able to move down
                    if board[self.row+1][self.col] * self.value <= 0:
                        res.append((1, 0))
                if self.col+1 <= self.j_max:    #able to move right
                    if board[self.row][self.col+1] * self.value <= 0:
                        if self.king_valid(board, (self.row, self.col), (0, 1)):
                            res.append((0, 1))
                if self.col-1 >= self.j_min:    #able to move left
                    if board[self.row][self.col-1] * self.value <= 0:
                        if self.king_valid(board, (self.row, self.col), (0, -1)):
                            res.append((0, -1))
        return res

class Knight(Piece):  # ma
    def __init__(self, color, position):
        self.name = 'knight'
        self.color = color
        self.value = piece_values[self.color + '_' + self.name]
        self.row = position[0]
        self.col = position[1]
        self.j_max = 8
        self.j_min = 0
        self.i_max = 9
        self.i_min = 0

    def next_valid_move(self, board):
        res = []
        if self.row-2 >= self.i_min and self.col+1 <= self.j_max:    #able to move up right 1
            if board[self.row-2][self.col+1] * self.value <= 0:
                if board[self.row-1][self.col] == 0:
                    if self.king_valid(board, (self.row, self.col), (-2, 1)):
                        res.append((-2, 1))
        if self.row-1 >= self.i_min and self.col+2 <= self.j_max:    #able to move up right 2
            if board[self.row-1][self.col+2] * self.value <= 0:
                if board[self.row][self.col+1] == 0:
                    if self.king_valid(board, (self.row, self.col), (-1, 2)):
                        res.append((-1, 2))
        if self.row+1 <= self.i_max and self.col+2 <= self.j_max:    #able to move down right 1
            if board[self.row+1][self.col+2] * self.value <= 0:
                if board[self.row][self.col+1] == 0:
                    if self.king_valid(board, (self.row, self.col), (1, 2)):
                        res.append((1, 2))
        if self.row+2 <= self.i_max and self.col+1 <= self.j_max:    #able to move down right 2
            if board[self.row+2][self.col+1] * self.value <= 0:
                if board[self.row+1][self.col] == 0:
                    if self.king_valid(board, (self.row, self.col), (2, 1)):
                        res.append((2, 1))
        if self.row+2 <= self.i_max and self.col-1 >= self.j_min:    #able to move down left 1
            if board[self.row+2][self.col-1] * self.value <= 0:
                if board[self.row+1][self.col] == 0:
                    if self.king_valid(board, (self.row, self.col), (2, -1)):
                        res.append((2, -1))
        if self.row+1 <= self.i_max and self.col-2 >= self.j_min:    #able to move down left 2
            if board[self.row+1][self.col-2] * self.value <= 0:
                if board[self.row][self.col-1] == 0:
                    if self.king_valid(board, (self.row, self.col), (1, -2)):
                        res.append((1, -2))
        if self.row-1 >= self.i_min and self.col-2 >= self.j_min:    #able to move up left 1
            if board[self.row-1][self.col-2] * self.value <= 0:
                if board[self.row][self.col-1] == 0:
                    if self.king_valid(board, (self.row, self.col), (-1, -2)):
                        res.append((-1, -2))
        if self.row-2 >= self.i_min and self.col-1 >= self.j_min:    #able to move up left 2
            if board[self.row-2][self.col-1] * self.value <= 0:
                if board[self.row-1][self.col] == 0:
                    if self.king_valid(board, (self.row, self.col), (-2, -1)):
                        res.append((-2, -1))
        return res