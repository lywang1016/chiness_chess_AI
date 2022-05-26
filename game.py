import time
from board import ChessBoard
from display import GUI
from player import HumanPlayer, AIPlayer

def main():
    chess_board = ChessBoard()
    gui = GUI()
    r_human = HumanPlayer('r')
    # b_human = HumanPlayer('b')
    b_ai = AIPlayer('b')
    while True:
        while True:
            # Red move
            if not r_human.check_moves(chess_board.board_states()):
                break
            while True:
                gui.update(chess_board.board_states())
                time.sleep(0.1)
                position = gui.check_event()
                if position:
                    r_human.update_board(chess_board.board_states())
                    if r_human.select_piece(position):
                        break
            while True:
                gui.update(chess_board.board_states())
                time.sleep(0.1)
                position = gui.check_event()
                if position:
                    r_human.update_board(chess_board.board_states())
                    move = r_human.take_action(position)
                    if move:
                        chess_board.move_piece(r_human.current_piece_posi, move)
                        break
            if chess_board.done:
                break
            # black move
            if not b_ai.check_moves(chess_board.board_states()):
                break
            posi, action = b_ai.select_action()
            chess_board.move_piece(posi, action)

            # if not b_human.check_moves(chess_board.board_states()):
            #     break
            # while True:
            #     gui.update(chess_board.board_states())
            #     time.sleep(0.1)
            #     position = gui.check_event()
            #     if position:
            #         b_human.update_board(chess_board.board_states())
            #         if b_human.select_piece(position):
            #             break
            # while True:
            #     gui.update(chess_board.board_states())
            #     time.sleep(0.1)
            #     position = gui.check_event()
            #     if position:
            #         b_human.update_board(chess_board.board_states())
            #         move = b_human.take_action(position)
            #         if move:
            #             chess_board.move_piece(b_human.current_piece_posi, move)
            #             break

            if chess_board.done:
                break
        chess_board.reset_board()

if __name__ == '__main__':
    main()
