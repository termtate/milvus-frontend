from ui.gui import UiInterface
from network.api import get_patients_by_ann_search, get_patients_by_fields, get_patients_by_id
from network.model import Patient
import pandas as pd

class Presenter:
    def __init__(self, view: UiInterface):
        self.view = view
    
    
    def common_search(self):
        text = self.view.get_search_text()
        self.view.clear_table()
        if text == '':
            self.view.show_critical_message('输入不能为空！')
            return
        
        if text.isdigit():
            res = get_patients_by_id(int(text))
        else:
            res = get_patients_by_fields(name=text)
        
        
        self.view.show_search_patients_number(len(res))
        self.view.show_patients_on_table(res)
        
    def advanced_search(self):
        text = self.view.get_search_text()
        field = self.view.get_advanced_search_field()
        self.view.clear_table()
        if text == '':
            self.view.show_critical_message('输入不能为空！')
            return

        res = get_patients_by_ann_search(query=text, field=field)
        
        self.view.show_search_patients_number(len(res))
        self.view.show_patients_on_table(res)
    
    def update_patient_field(self, row: int, column: int):
        # TODO 根据修改的单元格更新数据
        pass

        
    def delete_all_patients(self):
        # TODO
        pass
    
    def upload_file_to_database(self):
        if len(self.view.file_path) == 0:
            self.view.add_log_text("请先选择文件夹路径！")
            return
        self._upload(self.view.file_path)
        self.view.add_log_text("导入成功！")
        self.view.clear_file_path()
        
    def _upload(self, path: str) -> list[Patient]:
        df = pd.read_excel(path)
        columns = tuple(df.columns)
        return [Patient(**dict(zip(columns, row))) for row in df.values.tolist()]
    