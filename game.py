import time
from board import ChessBoard
from display import GUI
from player import HumanPlayer

def main():
    chess_board = ChessBoard()
    gui = GUI()
    r_human = HumanPlayer('r')
    b_human = HumanPlayer('b')
    while True:
        # Red move
        while True:
            gui.update(chess_board.board_states())
            time.sleep(0.1)
            position = gui.check_event()
            if position:
                r_human.update_board(chess_board.board_states())
                r_human.select_piece(position)
                break
        while True:
            gui.update(chess_board.board_states())
            time.sleep(0.1)
            position = gui.check_event()
            if position:
                r_human.update_board(chess_board.board_states())
                move = r_human.take_action(position)
                chess_board.move_piece(r_human.current_piece_posi, move)
                break
        # black move
        while True:
            gui.update(chess_board.board_states())
            time.sleep(0.1)
            position = gui.check_event()
            if position:
                b_human.update_board(chess_board.board_states())
                b_human.select_piece(position)
                break
        while True:
            gui.update(chess_board.board_states())
            time.sleep(0.1)
            position = gui.check_event()
            if position:
                b_human.update_board(chess_board.board_states())
                move = b_human.take_action(position)
                chess_board.move_piece(b_human.current_piece_posi, move)
                break

if __name__ == '__main__':
    main()
