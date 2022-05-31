from game import Game
from utils import print_dataset

def main():
    # game = Game(r_type='human', b_type='human', if_record=True, if_dataset=True)
    # game = Game(r_type='ai', b_type='ai', if_record=False, if_dataset=True, if_gui=False, gui_update=0.5)
    game = Game(r_type='human', b_type='ai', if_record=False, if_dataset=True)
    # game = Game(r_type='ai', b_type='human', if_record=False, if_dataset=True)
    for i in range(1000):
        game.episode()
        print_dataset(game.chess_board.dataset)

if __name__ == '__main__':
    main()