from piece import King, Warrior, Minister, Rook, Cannon, Pawn, Knight

class HumanPlayer:
    def __init__(self, color):
        self.color = color
        self.faction = 1
        if color == 'b':
            self.faction = -1
        self.current_board = None
        self.current_piece_value = 0
        self.current_piece_posi = None
        self.cadidate_move = []
    
    def update_board(self, board):
        self.current_board = board

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
                return True
            else:
                return False
        else:
            self.current_piece_value = 0
            self.current_piece_posi = None
            return False

    def action_valid(self, candidate_move, posi):
        candidate_target_posi = {}
        for move in candidate_move:
            target_posi = (self.current_piece_posi[0]+move[0], self.current_piece_posi[1]+move[1])
            candidate_target_posi[target_posi] = move
        if posi in candidate_target_posi:
            self.candidate_move = []
            return candidate_target_posi[posi]
        else:
            return None
        
    def take_action(self, posi):
        if self.current_piece_value != 0:
            return self.action_valid(self.candidate_move, posi)
            # value = abs(self.current_piece_value)
            # if value == 1:
            #     rook = Rook(self.color, self.current_piece_posi)
            #     candidate_move = rook.next_valid_move(self.current_board)
            #     return self.action_valid(candidate_move, posi)
            # if value == 2:
            #     knight = Knight(self.color, self.current_piece_posi)
            #     candidate_move = knight.next_valid_move(self.current_board)
            #     return self.action_valid(candidate_move, posi)
            # if value == 3:
            #     cannon = Cannon(self.color, self.current_piece_posi)
            #     candidate_move = cannon.next_valid_move(self.current_board)
            #     return self.action_valid(candidate_move, posi)
            # if value == 4:
            #     minister = Minister(self.color, self.current_piece_posi)
            #     candidate_move = minister.next_valid_move(self.current_board)
            #     return self.action_valid(candidate_move, posi)
            # if value == 5:
            #     warrior = Warrior(self.color, self.current_piece_posi)
            #     candidate_move = warrior.next_valid_move(self.current_board)
            #     return self.action_valid(candidate_move, posi)
            # if value == 6:
            #     pawn = Pawn(self.color, self.current_piece_posi)
            #     candidate_move = pawn.next_valid_move(self.current_board)
            #     return self.action_valid(candidate_move, posi)
            # if value == 7:
            #     king = King(self.color, self.current_piece_posi)
            #     candidate_move = king.next_valid_move(self.current_board)
            #     return self.action_valid(candidate_move, posi)

