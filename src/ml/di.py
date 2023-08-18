from injector import Module, provider, Injector, inject, singleton
from LAC import LAC
from ml.config import settings

from ml.recognize import Recognizer
from ppocr import PPOcr

class RecognizerModule(Module):
    # @singleton
    # @provider
    # def provide_paddleocr(self) -> PaddleOCR:
    #     return PaddleOCR(use_angle_cls=True, lang="ch")
    
    @singleton
    @provider
    def provide_ppocr(self) -> PPOcr:
        return PPOcr(
            exePath=str(settings.PPOCR_PATH)
        )

    @singleton
    @provider
    def provide_lac(self) -> LAC:
        return LAC(mode="lac")
    
    # @singleton
    # @provider
    # def provide_recognizer(self, paddleocr: PaddleOCR) -> Recognizer:
    #     pass