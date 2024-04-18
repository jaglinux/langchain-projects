import numpy as np
import torch

nd_array = np.loadtxt("./pytorch/linear/data.csv", delimiter=",")
t = torch.from_numpy(nd_array)
x = t[:, : -1]
y = t[:, -1:]