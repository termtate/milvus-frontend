from ml.predict import read_generated_txt
from ml.model import Model
from LAC import LAC

lac = LAC(mode="lac")

read_generated_txt(lac, r"I:\projects\python\milvus-frontend\assets\test\epilepsy case1-tonghaoxuan.docx.txt")