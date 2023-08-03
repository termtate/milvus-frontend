# from utils import *
# from model import *
# from config import *
from ml.utils import Dataset, data, collate_fn
from ml.model import Model
from ml.config import settings
import torch


if __name__ == '__main__':
    dataset = Dataset()
    loader = data.DataLoader(
        dataset,
        batch_size=100,
        shuffle=True,
        collate_fn=collate_fn,
    )

    model = Model().to(settings.DEVICE)
    optimizer = torch.optim.Adam(model.parameters(), lr=settings.LR)

    for e in range(settings.EPOCH):
        for b, (input, target, mask) in enumerate(loader):

            input = input.to(settings.DEVICE)
            mask = mask.to(settings.DEVICE)
            target = target.to(settings.DEVICE)

            y_pred = model(input, mask)
            loss = model.loss_fn(input, target, mask)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            if b % 10 == 0:
                print('>> epoch:', e, 'loss:', loss.item())
        if e % 100 == 0:
            torch.save(model, f'{settings.MODEL_DIR}model_{e}.pth')