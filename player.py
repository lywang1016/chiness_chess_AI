import copy
import numpy as np
from board import ChessBoard
from piece import King, Warrior, Minister, Rook, Cannon, Pawn, Knight
from constant import piece_values

class Player():
    def __init__(self, color):
        self.color = color
        self.faction = 1
        if color == 'b':
            self.faction = -1
        self.current_board = None
        self.current_piece_value = 0
        self.current_piece_posi = None
        self.cadidate_move = []
        self.all_move = {}
    
    def check_moves(self):
        self.all_move = {}
        for i in range(10):
            for j in range(9):
                if self.current_board[i][j] * self.faction > 0:
                    value = abs(self.current_board[i][j])
                    if value == 1:
                        rook = Rook(self.color, (i, j))
                        moves = rook.next_valid_move(self.current_board)
                        if len(moves) > 0:
                            self.all_move[(i,j)] = moves
                    if value == 2:
                        knight = Knight(self.color, (i, j))
                        moves = knight.next_valid_move(self.current_board)
                        if len(moves) > 0:
                            self.all_move[(i,j)] = moves
                    if value == 3:
                        cannon = Cannon(self.color, (i, j))
                        moves = cannon.next_valid_move(self.current_board)
                        if len(moves) > 0:
                            self.all_move[(i,j)] = moves
                    if value == 4:
                        minister = Minister(self.color, (i, j))
                        moves = minister.next_valid_move(self.current_board)
                        if len(moves) > 0:
                            self.all_move[(i,j)] = moves
                    if value == 5:
                        warrior = Warrior(self.color, (i, j))
                        moves = warrior.next_valid_move(self.current_board)
                        if len(moves) > 0:
                            self.all_move[(i,j)] = moves
                    if value == 6:
                        pawn = Pawn(self.color, (i, j))
                        moves = pawn.next_valid_move(self.current_board)
                        if len(moves) > 0:
                            self.all_move[(i,j)] = moves
                    if value == 7:
                        king = King(self.color, (i, j))
                        moves = king.next_valid_move(self.current_board)
                        if len(moves) > 0:
                            self.all_move[(i,j)] = moves
        if len(self.all_move) > 0:
            return True
        else:
            return False
    
    def update_board(self, board):
        self.current_board = copy.deepcopy(board)
class HumanPlayer(Player):
    def __init__(self, color):
        self.color = color
        self.faction = 1
        if color == 'b':
            self.faction = -1
        self.current_board = None
        self.current_piece_value = 0
        self.current_piece_posi = None
        self.cadidate_move = []
        self.all_move = {}
        self.stage = 'pick'
        self.move = None

    def reset(self):
        self.current_board = None
        self.current_piece_value = 0
        self.current_piece_posi = None
        self.cadidate_move = []
        self.all_move = {}
        self.stage = 'pick'
        self.move = None

    def select_piece(self, posi):
        if self.current_board[posi[0]][posi[1]] * self.faction > 0:
            self.current_piece_value = self.current_board[posi[0]][posi[1]]
            self.current_piece_posi = posi
            value = abs(self.current_piece_value)
            if value == 1:
                rook = Rook(self.color, self.current_piece_posi)
                self.candidate_move = rook.next_valid_move(self.current_board)
            if value == 2:
                knight = Knight(self.color, self.current_piece_posi)
                self.candidate_move = knight.next_valid_move(self.current_board)
            if value == 3:
                cannon = Cannon(self.color, self.current_piece_posi)
                self.candidate_move = cannon.next_valid_move(self.current_board)
            if value == 4:
                minister = Minister(self.color, self.current_piece_posi)
                self.candidate_move = minister.next_valid_move(self.current_board)
            if value == 5:
                warrior = Warrior(self.color, self.current_piece_posi)
                self.candidate_move = warrior.next_valid_move(self.current_board)
            if value == 6:
                pawn = Pawn(self.color, self.current_piece_posi)
                self.candidate_move = pawn.next_valid_move(self.current_board)
            if value == 7:
                king = King(self.color, self.current_piece_posi)
                self.candidate_move = king.next_valid_move(self.current_board)
            if len(self.candidate_move) > 0:
                self.stage = 'go'
        else:
            self.current_piece_value = 0
            self.current_piece_posi = None

    def action_valid(self, posi):
        candidate_target_posi = {}
        for move in self.candidate_move:
            target_posi = (self.current_piece_posi[0]+move[0], self.current_piece_posi[1]+move[1])
            candidate_target_posi[target_posi] = move
        if posi in candidate_target_posi:
            self.candidate_move = []
            self.stage = 'pick'
            self.move = candidate_target_posi[posi]
        else:
            self.move = None

class AIPlayer(Player):
    def __init__(self, color):
        self.color = color
        self.faction = 1
        self.board = ChessBoard()
        self.current_board = None
        self.current_piece_value = 0
        self.current_piece_posi = None
        self.cadidate_move = []
        self.all_move = {}

    def reset(self):
        self.current_board = None
        self.current_piece_value = 0
        self.current_piece_posi = None
        self.cadidate_move = []
        self.all_move = {}

    def update_board(self, board):
        self.board.load_board(board)
        if self.color == 'b':       # rotate board
            self.board.rotate_board()
        self.current_board = self.board.board_states()

    def check_moves(self):
        self.all_move = {}
        for i in range(10):
            for j in range(9):
                if self.current_board[i][j] * self.faction > 0:
                    value = abs(self.current_board[i][j])
                    if value == 1:
                        rook = Rook('r', (i, j))
                        moves = rook.next_valid_move(self.current_board)
                        if len(moves) > 0:
                            self.all_move[(i,j)] = moves
                    if value == 2:
                        knight = Knight('r', (i, j))
                        moves = knight.next_valid_move(self.current_board)
                        if len(moves) > 0:
                            self.all_move[(i,j)] = moves
                    if value == 3:
                        cannon = Cannon('r', (i, j))
                        moves = cannon.next_valid_move(self.current_board)
                        if len(moves) > 0:
                            self.all_move[(i,j)] = moves
                    if value == 4:
                        minister = Minister('r', (i, j))
                        moves = minister.next_valid_move(self.current_board)
                        if len(moves) > 0:
                            self.all_move[(i,j)] = moves
                    if value == 5:
                        warrior = Warrior('r', (i, j))
                        moves = warrior.next_valid_move(self.current_board)
                        if len(moves) > 0:
                            self.all_move[(i,j)] = moves
                    if value == 6:
                        pawn = Pawn('r', (i, j))
                        moves = pawn.next_valid_move(self.current_board)
                        if len(moves) > 0:
                            self.all_move[(i,j)] = moves
                    if value == 7:
                        king = King('r', (i, j))
                        moves = king.next_valid_move(self.current_board)
                        if len(moves) > 0:
                            self.all_move[(i,j)] = moves
        for posi in self.all_move: # if able to take black king, the only valid action is take the king
            for move in self.all_move[posi]:
                if self.current_board[posi[0]+move[0]][posi[1]+move[1]] == piece_values['b_king']:
                    self.all_move = {}
                    self.all_move[posi] = [move]
                    return True
        if len(self.all_move) > 0:
            return True
        else:
            return False

    def rotate_action(self, posi, move):
        move_ = (-move[0], -move[1])
        posi_ = (9 - posi[0], 8 - posi[1])
        return posi_, move_

    def random_action(self):
        posi_num = len(self.all_move)
        posi_idx = np.random.randint(posi_num)
        idx = 0
        for key in self.all_move:
            if idx == posi_idx:
                posi = key
                break
            idx += 1
        move_num = len(self.all_move[posi])
        move_idx = np.random.randint(move_num)
        idx = 0
        for moves in self.all_move[posi]:
            if idx == move_idx:
                move = moves
                break
            idx += 1
        if self.color == 'b':       # rotate move
            return self.rotate_action(posi, move)
        return posi, move