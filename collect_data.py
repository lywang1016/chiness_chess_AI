from game import Game
from utils import print_dataset

def main():
    # game = Game(r_type='human', b_type='human', if_record=True)
    # game = Game(r_type='ai', b_type='ai', if_record=False, if_gui=False, gui_update=0.5)
    game = Game(r_type='human', b_type='ai', if_record=False)
    # game = Game(r_type='ai', b_type='human', if_record=False)
    for i in range(1000):
        game.episode()
        # print_dataset(game.chess_board.dataset)

if __name__ == '__main__':
    main()