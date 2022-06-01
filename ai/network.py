import torch
import torch.nn as nn

class DQN(nn.Module):
    def __init__(self, h=10, w=9, outputs=1):
        super(DQN, self).__init__()
        self.conv1 = nn.Conv2d(1, 8, kernel_size=3, stride=1, padding=1)
        self.bn1 = nn.BatchNorm2d(8)
        self.conv2 = nn.Conv2d(8, 32, kernel_size=3, stride=1, padding=1)
        self.bn2 = nn.BatchNorm2d(32)
        self.conv3 = nn.Conv2d(32, 32, kernel_size=3, stride=1, padding=1)
        self.bn3 = nn.BatchNorm2d(32)

        def conv2d_size_out(size, kernel_size = 3, stride = 1, padding = 1):
            return (size + 2*padding - (kernel_size - 1) - 1) // stride  + 1
        convw = conv2d_size_out(conv2d_size_out(conv2d_size_out(w)))
        convh = conv2d_size_out(conv2d_size_out(conv2d_size_out(h)))
        fc_dim_input = convw * convh * 32

        self.fc_1 = nn.Linear(fc_dim_input, 2*fc_dim_input)
        self.bn_1 = nn.BatchNorm1d(2*fc_dim_input)
        self.fc_2 = nn.Linear(2*fc_dim_input, fc_dim_input)
        self.bn_2 = nn.BatchNorm1d(fc_dim_input)
        self.fc_3 = nn.Linear(fc_dim_input, 32*outputs)
        self.bn_3 = nn.BatchNorm1d(32*outputs)

        self.fc_out = nn.Linear(32*outputs, outputs)
        self.bn_out = nn.BatchNorm1d(outputs)

        self.relu = nn.LeakyReLU()

    def forward(self, state):
        batch_size = state.shape[0]
        state = state.view(batch_size, 1, 10, 9)
        x = self.relu(self.bn1(self.conv1(state)))
        x = self.relu(self.bn2(self.conv2(x)))
        x = self.relu(self.bn3(self.conv3(x)))
        x = self.relu(self.bn_1(self.fc_1(x.view(x.size(0), -1))))
        x = self.relu(self.bn_2(self.fc_2(x)))
        x = self.relu(self.bn_3(self.fc_3(x)))
        y = self.bn_out(self.fc_out(x))
        return y