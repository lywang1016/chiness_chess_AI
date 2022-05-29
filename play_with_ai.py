import time
from board import ChessBoard
from display import GUI
from player import HumanPlayer, AIPlayer

def main():
    chess_board = ChessBoard()
    gui = GUI()
    red = True

    human_color = input('Choose human color, input r for red, b for black.')
    if human_color == 'r':
        ai = AIPlayer('b')
        human = HumanPlayer('r')
    else:
        ai = AIPlayer('r')
        human = HumanPlayer('b')

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
            elif info == 'turn180':
                print('turn180')
                chess_board.rotate_board()
                red = not red
                ai.reset()
                human.reset()
            elif info == 'grid':
                if human_color == 'r':
                    if red: #check whos turn (red move)
                        if human.stage == 'pick':
                            human.select_piece(position)
                        if human.stage == 'go':
                            human.action_valid(position)
                            if human.move:
                                chess_board.move_piece(human.current_piece_posi, human.move)
                                red = not red
                else:
                    if not red: #check whos turn (red move)
                        if human.stage == 'pick':
                            human.select_piece(position)
                        if human.stage == 'go':
                            human.action_valid(position)
                            if human.move:
                                chess_board.move_piece(human.current_piece_posi, human.move)
                                red = not red
            else:
                if human_color == 'r':
                    if red:
                        human.update_board(chess_board.board_states())
                        if not human.check_moves():
                            chess_board.win = 'b'
                            break
                    else:
                        ai.update_board(chess_board.board_states())
                        if not ai.check_moves():
                            chess_board.win = 'r'
                            break
                        posi, move = ai.random_action()
                        chess_board.move_piece(posi, move)
                        red = not red
                else:
                    if not red:
                        human.update_board(chess_board.board_states())
                        if not human.check_moves():
                            chess_board.win = 'b'
                            break
                    else:
                        ai.update_board(chess_board.board_states())
                        if not ai.check_moves():
                            chess_board.win = 'r'
                            break
                        posi, move = ai.random_action()
                        chess_board.move_piece(posi, move)
                        red = not red
        if chess_board.win == 'r':
            print('Red Win!')
        else:
            print('Black Win!')
        chess_board.reset_board()
        ai.reset()
        human.reset()
        red = True

if __name__ == '__main__':
    main()