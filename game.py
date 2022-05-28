import time
from board import ChessBoard
from display import GUI
from player import HumanPlayer, AIPlayer

# class Game():
#     def __init__(self, r_type, b_type):
#         self.board = ChessBoard()
#         self.gui = GUI()
#         self.r_type = r_type
#         self.b_type = b_type
#         if r_type == 'human':
#             self.player_r = HumanPlayer('r')
#         if b_type == 'human':
#             self.player_b = HumanPlayer('b')
#         self.turn = True
#         self.done = False
#         # self.gui.update(self.board.board_states())

    # def step(self):
    #     if self.turn:   # Red move
    #         self.player_r.update_board(self.board.board_states())
    #         self.player_r.check_moves()
    #         if self.r_type == 'human':


    #     else:           # Black move
    #         self.player_b.update_board(self.board.board_states())
    #         self.player_b.check_moves()
    #     self.turn = not self.turn

def main():
    chess_board = ChessBoard()
    gui = GUI()
    red = True
    r_human = HumanPlayer('r')
    b_human = HumanPlayer('b')
    # b_ai = AIPlayer('b')
    while True:
        while not chess_board.done:
            if red:
                gui.update(chess_board.board_states(), 'r')
            else:
                gui.update(chess_board.board_states(), 'b')
            time.sleep(0.1)
            info, position = gui.check_event()

            if info == 'reset':
                print('reset')
                break
            if info == 'turn180':
                print('turn180')
                chess_board.rotate_board()
                red = not red
            if info == 'grid':
                if red: #check whos turn (red move)
                    r_human.update_board(chess_board.board_states())
                    if not r_human.check_moves():
                        break
                    if r_human.stage == 'pick':
                        r_human.select_piece(position)
                    if r_human.stage == 'go':
                        r_human.action_valid(position)
                        if r_human.move:
                            chess_board.move_piece(r_human.current_piece_posi, r_human.move)
                            red = not red
                else:   #black move
                    b_human.update_board(chess_board.board_states())
                    if not b_human.check_moves():
                        break
                    if b_human.stage == 'pick':
                        b_human.select_piece(position)
                    if b_human.stage == 'go':
                        b_human.action_valid(position)
                        if b_human.move:
                            chess_board.move_piece(b_human.current_piece_posi, b_human.move)
                            red = not red
        chess_board.reset_board()
        r_human.reset()
        b_human.reset()

if __name__ == '__main__':
    main()
