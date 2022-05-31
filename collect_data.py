import h5py
import numpy as np
from framework.game import Game
from framework.utils import merge_dataset, board_to_key, key_to_board

def main():
    # Load previous dataset
    fx = h5py.File("dataset/x.hdf5", "a")
    fx.close()
    fy = h5py.File("dataset/y.hdf5", "a")
    fy.close()
    dataset = {}
    fx = h5py.File('dataset/x.hdf5', 'r')
    fy = h5py.File('dataset/y.hdf5', 'r')
    for key in fx:
        board = np.array(fx[key])
        data = np.array(fy[key])
        dataset[board_to_key(board)] = data
    fx.close()
    fy.close()

    # game = Game(r_type='human', b_type='human', if_record=False, if_dataset=True)
    # game = Game(r_type='ai', b_type='ai', if_record=True, if_dataset=True, if_gui=False, gui_update=0.5)
    game = Game(r_type='human', b_type='ai', if_record=False, if_dataset=True)
    # game = Game(r_type='ai', b_type='human', if_record=True, if_dataset=True)

    for i in range(10):
        game.episode()
        merge_dataset(dataset, game.chess_board.dataset)

    fx = h5py.File("dataset/x.hdf5", "a")
    fy = h5py.File("dataset/y.hdf5", "a")
    for key in dataset:
        if str(key) in fx:
            data_in_file = np.array(fy[str(key)])
            for i in range(3):
                data_in_file[i] += dataset[key][i]
            del fy[str(key)]
            fy.create_dataset(str(key), data=data_in_file)
        else:
            fx.create_dataset(str(key), data=key_to_board(key))
            fy.create_dataset(str(key), data=dataset[key])
    fx.close()
    fy.close()

if __name__ == '__main__':
    main()