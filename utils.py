def rotate_action(posi, move):
        move_ = (-move[0], -move[1])
        posi_ = (9 - posi[0], 8 - posi[1])
        return posi_, move_

def board_turn180(board_in):
        board = board_in[::-1,::-1]
        for i in range(10):
            for j in range(9):
                board[i][j] = -board[i][j]
        return board