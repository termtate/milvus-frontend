import re
import torch
from torch.utils import data

import pandas as pd
from seqeval.metrics import classification_report
from ml.config import settings

def get_vocab():
    df = pd.read_csv(settings.VOCAB_PATH, names=['word', 'id'])
    return list(df['word']), dict(df.values)


def get_label():
    df = pd.read_csv(settings.LABEL_PATH, names=['label', 'id'])
    return list(df['label']), dict(df.values)


class Details:
    def __init__(self, row):
        self.info = row

class Dataset(data.Dataset):

    def __init__(self, type='train', base_len=50):
        super().__init__()
        self.base_len = base_len
        sample_path = settings.TRAIN_SAMPLE_PATH if type == 'train' else settings.TEST_SAMPLE_PATH
        self.df = pd.read_csv(sample_path, names=['word', 'label'])
        _, self.word2id = get_vocab()
        _, self.label2id = get_label()
        self.get_points()

    def get_points(self):
        self.points = [0]
        i = 0
        while True:
            if i + self.base_len >= len(self.df):
                self.points.append(len(self.df))
                break
            if self.df.loc[i + self.base_len, 'label'] == 'O':
                i += self.base_len
                self.points.append(i)
            else:
                i += 1

    def __len__(self):  
        return len(self.points) - 1

    def __getitem__(self, index):
        df = self.df[self.points[index]:self.points[index + 1]]
        word_unk_id = self.word2id[settings.WORD_UNK]
        label_o_id = self.label2id['O']
        input = [self.word2id.get(w, word_unk_id) for w in df['word']]
        target = [self.label2id.get(l, label_o_id) for l in df['label']]
        return input, target


def collate_fn(batch):
    batch.sort(key=lambda x: len(x[0]), reverse=True)
    max_len = len(batch[0][0])
    input = []
    target = []
    mask = []
    for item in batch:
        pad_len = max_len - len(item[0])
        input.append(item[0] + [settings.WORD_PAD_ID] * pad_len)
        target.append(item[1] + [settings.LABEL_O_ID] * pad_len)
        mask.append([1] * len(item[0]) + [0] * pad_len)
    return torch.tensor(input), torch.tensor(target), torch.tensor(mask).bool()


def extract(label, text):   # 从输出标签提取实体
    i = 0
    res = []
    while i < len(label):
        if label[i] != 'O':
            prefix, name = label[i].split('-')
            start = end = i
            i += 1
            while i < len(label) and label[i] == 'I-' + name:
                end = i
                i += 1
            res.append([name, text[start:end + 1]])
        else:
            i += 1
    return res


def report(y_true, y_pred):
    return classification_report(y_true, y_pred)


# 标签列表
def label_list():
    labels, _ = get_label()
    i = 1
    names = []
    while i < len(labels):
        _, name = labels[i].split('-')
        names.append(name)
        i += 1
    uniques = list(set(names))
    uniques.sort(key=names.index)
    return uniques



# 读取姓名年龄等
def read_info(text):
    # print(text)
    text = text.replace(' ', '')
    pat0 = re.compile(r'入院记录\(.*?\)|入院记录（.*?）|第\(.*?\)次入院记录|第(.*?)次入院记录', re.I)
    pat1 = re.compile(r'姓名[：:].*病室', re.I)
    pat2 = re.compile(r'住院号[：:]\d*', re.I)
    pat3 = re.compile(r'性别[：:].*民族', re.I)
    pat4 = re.compile(r'年龄[：:].*住址', re.I)
    pat5 = re.compile(r'电话[：:]\d*', re.I)
    pat6 = re.compile(r'表现为.*?[。；;.]', re.I)
    pat7 = re.compile(r'大约持续\d*秒|大约持续\d*分钟', re.I)
    pat8 = re.compile(r'每年发作\d*次|每月发作\d*次|每周发作\d*次|每日发作\d*次', re.I)
    pat9 = re.compile(r'其母怀孕时\d*岁|母孕时\d*岁', re.I)
    pat10 = re.compile(r'G\d*P\d*', re.I)
    pat11 = re.compile(r'出生体重\d*kg|出生体重\d*公斤', re.I)
    pat12 = re.compile(r'头围\d*cm', re.I)
    pat13 = re.compile(r'血、尿代谢筛查正常|血、尿代谢筛查.*?[,，.。；;]', re.I)
    pat14 = re.compile(r'铜兰蛋白正常|铜兰蛋白.*?[,，.。；;]', re.I)
    pat15 = re.compile(r'脑脊液.*?[,，.。；;]', re.I)
    pat16 = re.compile(r'基因检查.*?[.。；;]', re.I)
    pat17 = re.compile(r'头部CT.*?[.。；;]', re.I)
    pat18 = re.compile(r'头部MRI.*?[.。；;]', re.I)
    pat19 = re.compile(r'脑电图.*?[.。；;]|EEG.*?[.。；;]', re.I)

    op = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
    for m in range(20):
        string = f'pat{str(m)}'
        temp = eval(string)
        op[m] = '' if temp.search(text) is None else temp.search(text).group(0)
    return [
        ['第几次住院', op[0]],
        ['姓名', op[1][3:-2]],
        ['病案号', op[2][4:]],
        ['性别', op[3][3:-2]],
        ['年龄', op[4][3:-2]],
        ['电话', op[5][3:]],
        ['发作演变过程', op[6]],
        ['发作持续时间', op[7]],
        ['发作频次', op[8]],
        ['母孕年龄', op[9]],
        ['孕次产出', op[10]],
        ['出生体重', op[11]],
        ['头围', op[12]],
        ['血、尿代谢筛查', op[13]],
        ['铜兰蛋白', op[14]],
        ['脑脊液', op[15]],
        ['基因检查', op[16]],
        ['头部CT', op[17]],
        ['头部MRI', op[18]],
        ['头皮脑电图', op[19]],
    ]



if __name__ == '__main__':
    dataset = Dataset()
    loader = data.DataLoader(dataset, batch_size=100, collate_fn=collate_fn)
    print(iter(loader).next())
