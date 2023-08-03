from ml.di import PaddleOCRModule
from ml.recognize import Recognizer
from injector import Injector
from ml.model import Model


injector = Injector([PaddleOCRModule()])
recognizer = injector.get(Recognizer)
recognizer.read_gen_txt(r"I:\projects\python\milvus-frontend\assets\test\epilepsy case1-tonghaoxuan.docx.txt")