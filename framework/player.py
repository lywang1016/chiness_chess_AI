import copy
import yaml
import random
import numpy as np
import torch
from heapq import heapify, heappop, heappush
from framework.piece import King, Warrior, Minister, Rook, Cannon, Pawn, Knight
from framework.utils import rotate_action, board_turn180, board_to_key
from framework.constant import piece_values
from ai.network import DQN

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
    def __init__(self, color, explore_rate=1):
        self.color = color
        self.explore_rate = explore_rate
        self.faction = 1
        self.current_board = None
        self.current_piece_value = 0
        self.current_piece_posi = None
        self.cadidate_move = []
        self.all_move = {}
        self.past_board = []
        self.past_actions = []
        if self.explore_rate < 1:
            self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            self.q_star = DQN().to(self.device)
            with open('ai/config.yaml') as f:
                self.config = yaml.load(f, Loader=yaml.FullLoader)
            checkpoint = torch.load(self.config['save_model_path'])
            self.q_star.load_state_dict(checkpoint['model_state_dict'])
            self.q_star.eval()

    def reset(self):
        self.current_board = None
        self.current_piece_value = 0
        self.current_piece_posi = None
        self.cadidate_move = []
        self.all_move = {}
        self.past_board = []
        self.past_actions = []
        if self.explore_rate < 1:
            checkpoint = torch.load(self.config['save_model_path'])
            self.q_star.load_state_dict(checkpoint['model_state_dict'])
            self.q_star.eval()

    def update_board(self, board, past_board, past_actions):
        if self.color == 'b':       # rotate board
            self.current_board = board_turn180(board)
        else:
            self.current_board = board
        self.past_board = past_board
        self.past_actions = past_actions

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

        current_key = board_to_key(copy.deepcopy(self.current_board)) # remove the previous same action
        if current_key in self.past_board:
            idx = self.past_board.index(current_key)
            previous_posi = self.past_actions[idx][0]
            if previous_posi in self.all_move:
                moves = self.all_move[previous_posi]
                previous_move = self.past_actions[idx][1]
                if previous_move in moves:
                    moves.remove(previous_move)
                    if len(moves) > 0:
                        self.all_move[previous_posi] = moves
                    else:
                        self.all_move.pop(previous_posi, None)

        if len(self.all_move) > 0:
            return True
        else:
            return False

    def __random_action(self):
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
            return rotate_action(posi, move)
        return posi, move

    def __exploit_action(self):
        queue = []
        heapify(queue)
        for posi in self.all_move:
            for move in self.all_move[posi]:
                next_board = copy.deepcopy(self.current_board)
                value = next_board[posi[0]][posi[1]]
                next_board[posi[0]][posi[1]] = 0
                next_board[posi[0]+move[0]][posi[1]+move[1]] = value
                state = torch.from_numpy(next_board).to(self.device)
                if str(self.device) == 'cuda':
                    state = state.view(1, 1, 10, 9).type(torch.cuda.FloatTensor)
                else:
                    state = state.view(1, 1, 10, 9).type(torch.FloatTensor)
                win_rate = self.q_star(state)
                win_rate = win_rate.cpu().detach().numpy()[0][0]
                heappush(queue, (-win_rate, (posi, move)))
        value, action = heappop(queue)
        if self.color == 'b':       # rotate move
            return rotate_action(action[0], action[1])
        return action[0], action[1]
    
    def ai_action(self):
        if self.explore_rate == 0:
            return self.__exploit_action()
        elif self.explore_rate == 1:
            return self.__random_action()
        else:
            sample = random.random()
            if sample > self.explore_rate:
                return self.__exploit_action()
            else:
                return self.__random_action()

