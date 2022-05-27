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

#     def step(self):
#         if self.turn:   # Red move
#             self.player_r.update_board(self.board.board_states())
#             self.player_r.check_moves()
#             if self.r_type == 'human':


#         else:           # Black move
#             self.player_b.update_board(self.board.board_states())
#             self.player_b.check_moves()
#         self.turn = not self.turn

def main():
    chess_board = ChessBoard()
    gui = GUI()
    r_human = HumanPlayer('r')
    b_human = HumanPlayer('b')
    # b_ai = AIPlayer('b')
    while True:
        while True:
            # Red move
            r_human.update_board(chess_board.board_states())
            if not r_human.check_moves():
                break
            while True:
                gui.update(chess_board.board_states())
                time.sleep(0.1)
                info, position = gui.check_event()
                if info == 'grid':
                    r_human.update_board(chess_board.board_states())
                    if r_human.select_piece(position):
                        break
            while True:
                gui.update(chess_board.board_states())
                time.sleep(0.1)
                info, position = gui.check_event()
                if info == 'grid':
                    r_human.update_board(chess_board.board_states())
                    move = r_human.take_action(position)
                    if move:
                        chess_board.move_piece(r_human.current_piece_posi, move)
                        break
            if chess_board.done:
                break
            # black move
            # if not b_ai.check_moves(chess_board.board_states()):
            #     break
            # posi, action = b_ai.select_action()
            # chess_board.move_piece(posi, action)

            b_human.update_board(chess_board.board_states())
            if not b_human.check_moves():
                break
            while True:
                gui.update(chess_board.board_states())
                time.sleep(0.1)
                info, position = gui.check_event()
                if info == 'grid':
                    b_human.update_board(chess_board.board_states())
                    if b_human.select_piece(position):
                        break
            while True:
                gui.update(chess_board.board_states())
                time.sleep(0.1)
                info, position = gui.check_event()
                if info == 'grid':
                    b_human.update_board(chess_board.board_states())
                    move = b_human.take_action(position)
                    if move:
                        chess_board.move_piece(b_human.current_piece_posi, move)
                        break

            if chess_board.done:
                break
        chess_board.reset_board()

if __name__ == '__main__':
    main()
