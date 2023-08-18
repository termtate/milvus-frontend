from ppocr import PPOcr
from ml.di import RecognizerModule
from injector import Injector

i = Injector([RecognizerModule()])
ocr = i.get(PPOcr)

r = ocr.run(r"C:\Users\DEL\Desktop\a.png")

print(r)