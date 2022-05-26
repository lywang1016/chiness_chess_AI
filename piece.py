from constant import piece_values

class Piece:
    def __init__(self, name, color, position):
        self.name = name
        self.color = color
        self.row = position[0]
        self.col = position[1]
    
    def next_valid_move():
        return 

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
                res.append((1, -1))
        if self.row-1 >= self.i_min and self.col-1 >= self.j_min:    #able to move up left
            if board[self.row-1][self.col-1] * self.value <= 0:
                res.append((-1, -1))
        if self.row+1 <= self.i_max and self.col+1 <= self.j_max:    #able to move down right
            if board[self.row+1][self.col+1] * self.value <= 0:
                res.append((1, 1))
        if self.row-1 >= self.i_min and self.col+1 <= self.j_max:    #able to move up right
            if board[self.row-1][self.col+1] * self.value <= 0:
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
                    res.append((2, -2))
        if self.row-2 >= self.i_min and self.col-2 >= self.j_min:    #able to move up left
            if board[self.row-2][self.col-2] * self.value <= 0:
                if board[self.row-1][self.col-1] == 0:
                    res.append((-2, -2))
        if self.row+2 <= self.i_max and self.col+2 <= self.j_max:    #able to move down right
            if board[self.row+2][self.col+2] * self.value <= 0:
                if board[self.row+1][self.col+1] == 0:
                    res.append((2, 2))
        if self.row-2 >= self.i_min and self.col+2 <= self.j_max:    #able to move up right
            if board[self.row-2][self.col+2] * self.value <= 0:
                if board[self.row-1][self.col+1] == 0:
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
            if board[self.row][self.col+col] == 0:
                res.append((0, col))
            else:
                if board[self.row][self.col+col] * self.value < 0:
                    res.append((0, col))
                break
        for col in range(-1, self.j_min-self.col-1, -1): #Move left
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
                        res.append((row, 0))
                    break
        flag = False
        for col in range(1, self.j_max-self.col+1): #Move right
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
                        res.append((0, 1))
                if self.col-1 >= self.j_min:    #able to move left
                    if board[self.row][self.col-1] * self.value <= 0:
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
                        res.append((0, 1))
                if self.col-1 >= self.j_min:    #able to move left
                    if board[self.row][self.col-1] * self.value <= 0:
                        res.append((0, -1))
        return res