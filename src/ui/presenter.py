from ui.gui import UiInterface
from network.api import get_patients_by_ann_search, get_patients_by_fields, get_patients_by_id
from network.model import Patient

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

        res = get_patients_by_ann_search(query=text)
        
        self.view.show_search_patients_number(len(res))
        self.view.show_patients_on_table(res)
    
    def update_patient_field(self, row: int, column: int):
        # TODO 根据
        pass

        
    def delete_all_patients(self):
        # TODO
        pass
    
    