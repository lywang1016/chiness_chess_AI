import time
from board import ChessBoard
from display import GUI
from player import HumanPlayer, AIPlayer

def human_vs_human():
    chess_board = ChessBoard()
    gui = GUI()
    red = True
    r_human = HumanPlayer('r')
    b_human = HumanPlayer('b')
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
                r_human.reset()
                b_human.reset()
            elif info == 'grid':
                if red: #check whos turn (red move)
                    if r_human.stage == 'pick':
                        r_human.select_piece(position)
                    if r_human.stage == 'go':
                        r_human.action_valid(position)
                        if r_human.move:
                            chess_board.move_piece(r_human.current_piece_posi, r_human.move, red)
                            red = not red
                else:   #black move
                    if b_human.stage == 'pick':
                        b_human.select_piece(position)
                    if b_human.stage == 'go':
                        b_human.action_valid(position)
                        if b_human.move:
                            chess_board.move_piece(b_human.current_piece_posi, b_human.move, red)
                            red = not red
            else:
                if red:
                    r_human.update_board(chess_board.board_states())
                    if not r_human.check_moves():
                        chess_board.set_done('b')
                        break
                else:
                    b_human.update_board(chess_board.board_states())
                    if not b_human.check_moves():
                        chess_board.set_done('r')
                        break
        if chess_board.win == 'r':
            print('Red Win!')
        else:
            print('Black Win!')
        chess_board.reset_board()
        r_human.reset()
        b_human.reset()
        red = True

def human_vs_ai():
    chess_board = ChessBoard(record = True)
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
                                chess_board.move_piece(human.current_piece_posi, human.move, red)
                                red = not red
                else:
                    if not red: #check whos turn (red move)
                        if human.stage == 'pick':
                            human.select_piece(position)
                        if human.stage == 'go':
                            human.action_valid(position)
                            if human.move:
                                chess_board.move_piece(human.current_piece_posi, human.move, red)
                                red = not red
            else:
                if human_color == 'r':
                    if red:
                        human.update_board(chess_board.board_states())
                        if not human.check_moves():
                            chess_board.set_done('b')
                            break
                    else:
                        ai.update_board(chess_board.board_states())
                        if not ai.check_moves():
                            chess_board.set_done('r')
                            break
                        posi, move = ai.random_action()
                        chess_board.move_piece(posi, move, red)
                        red = not red
                else:
                    if not red:
                        human.update_board(chess_board.board_states())
                        if not human.check_moves():
                            chess_board.set_done('b')
                            break
                    else:
                        ai.update_board(chess_board.board_states())
                        if not ai.check_moves():
                            chess_board.set_done('r')
                            break
                        posi, move = ai.random_action()
                        chess_board.move_piece(posi, move, red)
                        red = not red
        if chess_board.win == 'r':
            print('Red Win!')
        else:
            print('Black Win!')
        chess_board.fill_dataset()
        print(chess_board.dataset)
        chess_board.save_csv()
        chess_board.reset_board()
        ai.reset()
        human.reset()
        red = True

def ai_vs_ai():
    chess_board = ChessBoard()
    # gui = GUI()
    red = True
    r_ai = AIPlayer('r')
    b_ai = AIPlayer('b')

    while True:
        while not chess_board.done:
            # if red:
            #     gui.update(chess_board.board_states(), 'r')
            # else:
            #     gui.update(chess_board.board_states(), 'b')
            # time.sleep(0.1)
            # info, position = gui.check_event()

            info = 'none'
            if info == 'reset':
                print('reset')
                break
            elif info == 'turn180':
                print('turn180')
                chess_board.rotate_board()
                red = not red
                r_ai.reset()
                b_ai.reset()
            else:
                if red:
                    r_ai.update_board(chess_board.board_states())
                    if not r_ai.check_moves():
                        chess_board.set_done('b')
                        break
                    posi, move = r_ai.random_action()
                    chess_board.move_piece(posi, move, red)
                    red = not red
                else:
                    b_ai.update_board(chess_board.board_states())
                    if not b_ai.check_moves():
                        chess_board.set_done('r')
                        break
                    posi, move = b_ai.random_action()
                    chess_board.move_piece(posi, move, red)
                    red = not red
        if chess_board.win == 'r':
            print('Red Win!')
        else:
            print('Black Win!')
        chess_board.reset_board()
        r_ai.reset()
        b_ai.reset()
        red = True

if __name__ == '__main__':
    # ai_vs_ai()
    human_vs_ai()
    # human_vs_human()