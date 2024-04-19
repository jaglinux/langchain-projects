import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

LR = 0.001
EPOCHS = 100
BATCH_SIZE = 10

nd_array = np.loadtxt("./pytorch/linear/data.csv", delimiter=",")
t = torch.tensor(nd_array, dtype=torch.float32)
x = t[:, : -1]
y = t[:, -1:]

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden1 = nn.Linear(8, 12)
        self.act1 = nn.ReLU()
        self.hidden2 = nn.Linear(12, 8)
        self.act2 = nn.ReLU()
        self.output = nn.Linear(8, 1)
        self.act_output = nn.Sigmoid()

    def forward(self, x):
        x = self.hidden1(x)
        x = self.act1(x)
        x = self.hidden2(x)
        x = self.act2(x)
        x = self.output(x)
        x = self.act_output(x)
        return x

model = NeuralNetwork()
print(model)
loss_fn = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=LR)

for i in range(EPOCHS):
    print(f" EPOCH : {i}")
    for j in range(0, len(x), BATCH_SIZE):
        batch_x = x[j:j+BATCH_SIZE]
        prediction_y = model(batch_x)
        batch_y = y[j:j+BATCH_SIZE]
        loss = loss_fn(prediction_y, batch_y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    print(f" EPOCH : {i} and last loss is {loss}")

with torch.no_grad():
    y_pred = model(x)

accuracy = (y_pred.round() == y).float().mean()
print(f"Accuracy {accuracy}")