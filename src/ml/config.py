from pathlib import Path
from pydantic_settings import BaseSettings
import torch

class Settings(BaseSettings):
    ORIGIN_DIR: str = './src/ml/input/origin/'
    ANNOTATION_DIR: str = './src/ml/output/annotation/'

    TRAIN_SAMPLE_PATH: str = './src/ml/output/train_sample.txt'
    TEST_SAMPLE_PATH: str = './src/ml/output/test_sample.txt'
    
    TXT_PATH: str = './src/ml/input/txt/'
    ANN_PATH: str = './src/ml/input/ann/'

    VOCAB_PATH: str = './src/ml/output/vocab.txt'
    LABEL_PATH: str = './src/ml/output/label.txt'

    WORD_PAD: str = '<PAD>'
    
    WORD_UNK: str = '<UNK>'

    WORD_PAD_ID: int = 0
    WORD_UNK_ID: int = 1
    LABEL_O_ID: int = 0

    VOCAB_SIZE: int = 3000
    EMBEDDING_DIM: int = 200
    HIDDEN_SIZE: int = 256
    TARGET_SIZE: int = 117
    LR: float = 1e-5
    EPOCH: int = 7001

    MODEL_DIR: str = './src/ml/output/model/'

    DBHOST: str  = 'localhost'
    DBUSER: str  = 'root'
    DBPASS: str  = '123456'
    DBNAME: str  = 'test1'


    DEVICE: str  = 'cuda' if torch.cuda.is_available() else 'cpu'
    
    PPOCR_PATH: Path = Path("PaddleOCR-json_v.1.3.0/PaddleOCR-json.exe")


settings = Settings()
