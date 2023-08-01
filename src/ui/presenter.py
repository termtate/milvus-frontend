from ui import UiInterface, TABLE_COLUMNS
from network.api import get_patients_by_ann_search, get_patients_by_fields, \
    get_patients_by_id, update_patient, create_patients, delete_all
from network.model import Patient
import pandas as pd
from pprint import pprint


colnums_name_map = {
    "ID": "id",
    "身份证号": "id_card_number",
    "姓名": "name",
    "第几次住院": "hospitalize_num",
    "病案号": "case_number",
    "性别": "sex",
    "年龄": "age",
    "电话": "phone_number",
    "发作演变过程": "seizure_evolution",
    "发作持续时间": "seizure_duration",
    "发作频次": "seizure_freq",
    "母孕年龄": "maternal_pregnancy_age",
    "孕次产出": "pregnancy_num",
    "出生体重": "birth_weight",
    "头围": "head_c",
    "血、尿代谢筛查": "blood_urine_screening",
    "铜兰蛋白": "copper_cyanin",
    "脑脊液": "csf",
    "基因检查": "genetic_test",
    "头部CT": "head_ct",
    "头部MRI": "head_mri",
    "头皮脑电图": "scalp_eeg",
    "诱发因素": "precipitating_factor",
}

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
        field = colnums_name_map[self.view.get_advanced_search_field()]
        self.view.clear_table()
        if text == '':
            self.view.show_critical_message('输入不能为空！')
            return
        # print(f"{text=}, {field=}")
        res = get_patients_by_ann_search(query=text, field=field)
        
        self.view.show_search_patients_number(len(res))
        self.view.show_patients_on_table(res)
    
    def update_patient_field(self, row: int, column: int):
        if not self.view.refreshing:
            column_name = colnums_name_map[TABLE_COLUMNS[column]]
            text = self.view.table.item(row, column).text()
            patient_id = int(self.view.table.item(row, 0).text())
            update_patient(patient_id, column_name, text)


        
    def delete_all_patients(self):
        return delete_all()
    
    def upload_file_to_database(self):
        if len(self.view.file_path) == 0:
            self.view.add_log_text("请先选择文件夹路径！")
            return
        patients = self._upload(self.view.file_path)
        create_patients(*patients)
        
        self.view.add_log_text("导入成功！")
        self.view.clear_file_path()
        
    def _upload(self, path: str) -> list[Patient]:

        df = pd.read_excel(path, dtype={
            "病案号": str,
            "电话": str
        }).rename(columns=colnums_name_map)[list(colnums_name_map.values())]
        columns = tuple(df.columns)
        return [Patient(**dict(zip(columns, row))) for row in df.values.tolist()]
    