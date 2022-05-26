import time
from utils import ChessBoard
from display import GUI


def main():
    chess_board = ChessBoard()
    gui = GUI()
    while True:
        position = gui.check_event()
        if position:
            print(position)
        gui.update(chess_board.board_states())
        time.sleep(0.1)

if __name__ == '__main__':
    main()
