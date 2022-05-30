from game import Game

def main():
    # game = Game(r_type='human', b_type='human', if_record=False)
    # game = Game(r_type='ai', b_type='ai', if_record=True, if_gui=False, gui_update=0.5)
    game = Game(r_type='human', b_type='ai', if_record=False)
    # game = Game(r_type='ai', b_type='human', if_record=False)
    for i in range(10):
        game.episode()

if __name__ == '__main__':
    main()