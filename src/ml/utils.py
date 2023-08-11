import re
from typing import Callable, Literal
import torch
from torch.utils import data
from LAC import LAC
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



def recognize_attribute(lac: LAC, text: str, pattern: Literal["姓名", "年龄", "性别"], cut_len: int = 8):
    '''
    :param text:
    :param pattern:需要识别的类型
    :param cut_len: 冒号后截取一定长度
    :return: str
    '''
    rec_pattern: dict[str, list[str]] = {
        "姓名": ["PER"],
        "年龄": ["m","TIME"],
        "性别": ["a"]
    }
    # rec_pattern={
    #     "name":["姓名",["PER"]],
    #     "age":["年龄",["m","TIME"]],
    #     "gender":["性别",["a"]]
    # }

    assert pattern in rec_pattern

    attribute = pattern
    _label_list = rec_pattern[pattern]
    pos = (
        text.find(f"{attribute}：")
        if f"{attribute}：" in text
        else text.find(f"{attribute}:")
    )
    if attribute == "性别":
        return text[pos + 3: pos + 4]
    _text=text[pos+3:pos+3+cut_len]                     #冒号后截取cut_len位
                              #加载模型
    result=lac.run(_text)                               #result[0]为分词list，[1]为标签list
    ans = [
        ((result[0][idx]).split())[0]
        for idx, label in enumerate(result[1])
        if label in _label_list
    ]
    # print(name[0])
    return "".join(ans) if ans else _text

# 读取姓名年龄等
def read_info(lac: LAC, text: str):
    def re_match(pattern: str) -> Callable[[str], str]:
        p = re.compile(pattern, re.I)
        def inner(s: str):
            res = p.search(s)
            return "" if res is None else res[0]

        return inner

    field_recognize_map: dict[str, Callable[[str], str]] = {
        "第几次住院": re_match(r'入院记录\(.*?\)|入院记录（.*?）|第\(.*?\)次入院记录|第(.*?)次入院记录'),
        '姓名': lambda text: recognize_attribute(lac, text, pattern="姓名"),
        '病案号': lambda text: re_match(r'住院号[：:]\d*')(text)[4:],
        '性别': lambda text: recognize_attribute(lac, text, pattern="性别"),
        '年龄': lambda text: recognize_attribute(lac, text, pattern="年龄"),
        '电话': lambda text: re_match(r'电话[：:]\d*')(text)[3:],
        '发作演变过程': re_match(r'表现为.*?[。；;.]'),
        '发作持续时间': re_match(r'大约持续\d*秒|大约持续\d*分钟'),
        '发作频次': re_match(r'每年发作\d*次|每月发作\d*次|每周发作\d*次|每日发作\d*次'),
        '母孕年龄': re_match(r'其母怀孕时\d*岁|母孕时\d*岁'),
        '孕次产出': re_match(r'G\d*P\d*'),
        '出生体重': re_match(r'出生体重\d*kg|出生体重\d*公斤'),
        '头围': re_match(r'头围\d*cm'),
        '血、尿代谢筛查': re_match(r'血、尿代谢筛查正常|血、尿代谢筛查.*?[,，.。；;]'),
        '铜兰蛋白': re_match(r'铜兰蛋白正常|铜兰蛋白.*?[,，.。；;]'),
        '脑脊液': re_match(r'脑脊液.*?[,，.。；;]'),
        '基因检查': re_match(r'基因检查.*?[.。；;]'), 
        '头部CT': re_match(r'头部CT.*?[.。；;]'), 
        '头部MRI': re_match(r'头部MRI.*?[.。；;]'), 
        '头皮脑电图': re_match(r'脑电图.*?[.。；;]|EEG.*?[.。；;]'),
    }
    
    res: list[tuple[str, str]] = []
    
    for field, search_func in field_recognize_map.items():
        res.append((field, search_func(text)))
    
    return res



if __name__ == '__main__':
    dataset = Dataset()
    loader = data.DataLoader(dataset, batch_size=100, collate_fn=collate_fn)
    print(iter(loader).next())
