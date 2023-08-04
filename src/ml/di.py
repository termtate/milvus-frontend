from injector import Module, provider, Injector, inject, singleton
from paddleocr import PaddleOCR

from ml.recognize import Recognizer

class PaddleOCRModule(Module):
    @singleton
    @provider
    def provide_paddleocr(self) -> PaddleOCR:
        return PaddleOCR(use_angle_cls=True, lang="ch")
    
    # @singleton
    # @provider
    # def provide_recognizer(self, paddleocr: PaddleOCR) -> Recognizer:
    #     pass