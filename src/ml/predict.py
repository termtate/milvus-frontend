from ml.config import settings
from ml.utils import get_label, get_vocab, extract, label_list, read_info
from pprint import pprint
import torch
from LAC import LAC

def read_generated_txt(lac: LAC, path: str):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
        return output_labels(lac, text)
            
    # 输出标签
def output_labels(lac: LAC, text):
    _, word2id = get_vocab()
    input_ = torch.tensor([[word2id.get(w, settings.WORD_UNK_ID) for w in text]]).to(settings.DEVICE)
    mask = torch.tensor([[1] * len(text)]).bool().to(settings.DEVICE)

    model = torch.load(f'{settings.MODEL_DIR}model_7000.pth', map_location=settings.DEVICE)
    y_pred = model(input_, mask)
    id2label, _ = get_label()

    label = [id2label[l] for l in y_pred[0]]
    # print(text)
    # print(label)
    info = extract(label, text)

    # pprint("------info-------")
    # pprint(info)
    # pprint('\n' * 3)
    # pprint("------text-------")
    # pprint(info)
    # print(info)
    # load_db(info, text)  # TODO
    # print()
    labels = label_list()
    # print(labels)
    output = [list(i) for i in read_info(lac, text)]
    # pprint(labels)
    output.extend([l, ''] for l in labels)
    
    for i, label_name in enumerate(labels, start=20):
        for per in info:
            if isinstance(per, list) and per[0] == label_name:
                if output[i][1] != '':
                    output[i][1] += '，'
                output[i][1] += per[1]
    
    return dict(output)

    # sqlstr = list(map(str, labels))
    # sqlstr = ','.join(sqlstr)
    # sqlstr = f'第几次住院,姓名,病案号,性别,年龄,电话,发作演变过程,发作持续时间,发作频次,母孕年龄,孕次产出,出生体重,头围,血、尿代谢筛查,铜兰蛋白,脑脊液,基因检查,头部CT,头部MRI,头皮脑电图,{sqlstr}'
    # # print(sqlstr)

    # aaa = ''
    # for i in range(78):
    #     if i != 0:
    #         aaa += ','
    #     aaa += '%s'

    # sql = f'INSERT INTO TABLE1({sqlstr}) VALUE ({aaa})'
    # value = [v[1] for v in output if isinstance(v, list)]
    # value = tuple(value)
    # # pprint(sql)
    # # pprint(value)