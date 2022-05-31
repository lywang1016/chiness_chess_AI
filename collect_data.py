import h5py
import numpy as np
from game import Game
from utils import print_dataset, merge_dataset, key_to_board, print_board

def main():
    f = h5py.File("dataset/x.hdf5", "a")
    f.close()
    f = h5py.File("dataset/y.hdf5", "a")
    f.close()

    # # game = Game(r_type='human', b_type='human', if_record=False, if_dataset=True)
    # game = Game(r_type='ai', b_type='ai', if_record=False, if_dataset=True, if_gui=False, gui_update=0.5)
    # # game = Game(r_type='human', b_type='ai', if_record=False, if_dataset=True)
    # # game = Game(r_type='ai', b_type='human', if_record=False, if_dataset=True)

    # dataset = {}
    # for i in range(100):
    #     game.episode()
    #     merge_dataset(dataset, game.chess_board.dataset)
    # # print_dataset(dataset)

    # f = h5py.File("dataset/x.hdf5", "a")
    # for key in dataset:
    #     f.create_dataset(str(key), data=key_to_board(key))
    # f.close()
    # f = h5py.File("dataset/y.hdf5", "a")
    # for key in dataset:
    #     # total = sum(dataset[key])
    #     # win_rate = dataset[key][0] / float(total)
    #     f.create_dataset(str(key), data=dataset[key])
    # f.close()

    f = h5py.File('dataset/x.hdf5', 'r')
    for key in f:
        data = np.array(f[key])
        # print(data)
        print_board(data)
        break
    f.close()

    f = h5py.File('dataset/y.hdf5', 'r')
    for key in f:
        data = np.array(f[key])
        print(data)
        break
    f.close()

if __name__ == '__main__':
    main()