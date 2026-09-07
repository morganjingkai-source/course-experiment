import torch
from torch import nn

x = torch.linspace(-1, 1, 101).reshape(-1, 1)
y = 3 * x - 1

model = nn.Linear(1, 1)
loss_fn = nn.MSELoss()
opt = torch.optim.SGD(model.parameters(), lr=0.1)

for _ in range(200):
    pred = model(x)
    loss = loss_fn(pred, y)

    opt.zero_grad()
    loss.backward()
    opt.step()

model.eval()

with torch.no_grad():
    pred = model(x)
    final_loss = loss_fn(pred, y)

    print("Final loss:", final_loss.item())
    print("Weight:", model.weight.item())
    print("Bias:", model.bias.item())
