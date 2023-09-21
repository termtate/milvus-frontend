from pathlib import Path
from typing import Any
from injector import inject
import os
from logging import getLogger
from ppocr import PPOcr
from ml.parse import parse_doc_file, parse_docx_file, parse_image, parse_pdf_file
from ml.predict import read_generated_txt
from LAC import LAC

logger = getLogger(__name__)


class Recognizer:
    @inject
    def __init__(self, ppocr: PPOcr, lac: LAC):
      self.ppocr = ppocr
      self.lac = lac
    
    def read_files2(self, file_path: str):
        path, name = os.path.split(file_path)
        self._recognize_from_file(path, name)

        # files=os.listdir(file_path)
        # res: list[dict[str, Any]] = []
        # for file in files:
        #     post_name=file.split(".")[-1]
        #     if post_name != "txt":
        #         continue
        #     res.append(read_generated_txt(self.lac, os.path.join(file_path, file)))
        
        return read_generated_txt(self.lac, f"{file_path}.txt")

    def _recognize_from_file(self, pathname: str, filename: str):
        '''为非txt格式的文件，在相同路径下生成对应的txt文件，命名为原文件名+.txt'''
        # TODO 把txt设置为临时文件
        complete_name = os.path.join(pathname, filename)

        file_type = filename.split(".")[-1]

        match file_type:
            case "txt":
                return
            case "docx":
                parse_docx_file(complete_name)
            
            case "doc":
                parse_doc_file(complete_name)
                
            case "pdf":
                parse_pdf_file(pathname, filename, pathname)
                
            case "png" | "jpg":
                parse_image(self.ppocr, complete_name)
            
            case _:
                logger.warning("Not Supported File Type")
    

