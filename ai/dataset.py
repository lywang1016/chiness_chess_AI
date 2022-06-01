import h5py
import numpy as np
from torch.utils.data import Dataset

class MyDataset(Dataset):
    def __init__(self, h5py_x_path='dataset/x.hdf5', h5py_y_path='dataset/y.hdf5'):
        self.board = []
        self.win_rate = []
        fx = h5py.File(h5py_x_path, 'r')
        fy = h5py.File(h5py_y_path, 'r')
        for key in fx:
            board = np.array(fx[key])
            data = np.array(fy[key])
            win_rate = float(data[0]) / (data[0]+data[1]+data[2])
            self.board.append(board)
            self.win_rate.append(win_rate)
        fx.close()
        fy.close()
        self.length = len(self.board)

    def __len__(self):
        return self.length

    def __getitem__(self, idx):
        sample = {'board': self.board[idx],
                  'win_rate': self.win_rate[idx]}
        return sample

