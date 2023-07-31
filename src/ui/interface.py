from network.model import Patient


from PySide2.QtWidgets import QTableWidgetItem, QTableWidget


from abc import ABC, abstractmethod


class UiInterface(ABC):
    @abstractmethod
    def clear_table(self):
        pass

    @abstractmethod
    def get_search_text(self) -> str:
        pass

    @abstractmethod
    def show_critical_message(self, msg: str):
        pass

    @abstractmethod
    def show_search_patients_number(self, num: int):
        pass

    @abstractmethod
    def show_patients_on_table(self, data: list[Patient]):
        pass

    @abstractmethod
    def get_advanced_search_field(self) -> str:
        pass

    @abstractmethod
    def add_log_text(self, text: str):
        pass

    @property
    @abstractmethod
    def file_path(self) -> str:
        pass

    @abstractmethod
    def get_table_item(self, row: int, col: int) -> QTableWidgetItem:
        pass

    @abstractmethod
    def clear_file_path(self):
        pass
    
    @property
    @abstractmethod
    def refreshing(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def table(self) -> QTableWidget:
        pass


TABLE_COLUMNS = (
    'ID', '身份证号', '姓名', '第几次住院', '病案号', '性别', '年龄',
    '电话', '发作演变过程', '发作持续时间', '发作频次', '母孕年龄',
    '孕次产出', '出生体重', '头围', '血、尿代谢筛查', '铜兰蛋白',
    '脑脊液', '基因检查', '头部CT', '头部MRI', '头皮脑电图', '诱发因素'
)
ANN_SEARCH_FIELDS = ("发作演变过程", ) # TODO 
    
    