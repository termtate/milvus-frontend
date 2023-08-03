import torch.nn as nn
from ml.config import settings
from torchcrf import CRF
import torch


class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.embed = nn.Embedding(settings.VOCAB_SIZE, settings.EMBEDDING_DIM, settings.WORD_PAD_ID)
        self.lstm = nn.LSTM(
            settings.EMBEDDING_DIM,
            settings.HIDDEN_SIZE,
            batch_first=True,
            bidirectional=True,
        )
        self.linear = nn.Linear(2 * settings.HIDDEN_SIZE, settings.TARGET_SIZE)
        self.crf = CRF(settings.TARGET_SIZE, batch_first=True)

    def _get_lstm_feature(self, input):
        out = self.embed(input)
        out, _ = self.lstm(out)
        return self.linear(out)

    def forward(self, input, mask):
        out = self._get_lstm_feature(input)
        return self.crf.decode(out, mask)

    def loss_fn(self, input, target, mask):
        y_pred = self._get_lstm_feature(input)
        return -self.crf.forward(y_pred, target, mask, reduction='mean')


# if __name__ == '__main__':
    # model = Model()
    # input = torch.randint(0, 732, (100, 50))
    # # print(input.shape)
    # # print(model)
    # print(len(model(input, None)))
    # print(model(input.to(DEVICE), None).shape)