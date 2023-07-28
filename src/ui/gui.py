from PySide2 import QtWidgets
from PySide2.QtWidgets import QTableWidgetItem, QWidget, QPushButton, QProgressBar
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMessageBox, QFileDialog, QTableWidget
from PySide2.QtCore import Slot
from network.api import get_patients_by_ann_search, get_patients_by_fields, get_patients_by_id
from network.model import Patient

from qt_material import apply_stylesheet

from abc import ABC, abstractmethod
from ui.presenter import Presenter

# import predict
# from config import *
# from predict import *


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
    
    
TABLE_COLUMNS = ('ID', "身份证号", '第几次住院', '姓名', '病案号', '性别', '年龄', '电话', '发作演变过程')


class TestWin(UiInterface):
    def __init__(self):
        # self.path = ''
        # self.search_state=0
        self.ui = QUiLoader().load('main.ui')
        self.presenter = Presenter(self)

        self.ui.searchButton.clicked.connect(self.presenter.common_search)
        self.ui.searchButton_3.clicked.connect(self.presenter.advanced_search)

        self.ui.stack1Button.clicked.connect(self.display1)
        self.ui.stack2Button.clicked.connect(self.display2)
        self.ui.list1.currentIndexChanged.connect(self.selectionchange1)
        self.ui.getpathbutton.clicked.connect(lambda: self.getfile(self.ui.getpathbutton))
        self.ui.getpathbutton.clicked.connect(lambda: self.getpath())
        self.ui.pushButton.clicked.connect(self.storage)
        self.ui.table.cellChanged.connect(self.presenter.update_patient_field)
        self.ui.pushButton_2.clicked.connect(self.presenter.delete_all_patients)
        self.ui.setWindowTitle('病历查询')
        # cnames = ['ID', "身份证号", '第几次住院', '姓名', '病案号', '性别', '年龄', '电话', '发作演变过程']
        self.ui.table.setColumnCount(len(TABLE_COLUMNS))
        self.ui.table.setHorizontalHeaderLabels(TABLE_COLUMNS)
        # self.flag = True
        # self.list = []
    
    
    def clear_table(self):
        self.ui.table.setRowCount(0)
    
    def get_search_text(self) -> str:
        return self.ui.searchtext1.text()
    
    def show_critical_message(self, msg: str):
        QMessageBox.critical(
            self.ui,
            '错误',
            msg
        )
    
    def show_search_patients_number(self, num: int):
        self.ui.numlabel1.setText(f'搜索结果：{num}人')
    
    def show_patients_on_table(self, data: list[Patient]):
        for i in range(len(data)):
            self.ui.table.insertRow(i)
            for index, value in enumerate(data[i].model_dump().values()):
                self.ui.table.setItem(i, index, QTableWidgetItem(str(value)))
                
    def get_advanced_search_field(self):
        return self.ui.list2.currentText()


    # def revise(self, row, column):  # 修改数据库
    #     if self.flag:
    #         columnname = self.ui.table.horizontalHeaderItem(column).text()
    #         value1 = self.ui.table.item(row, column).text()
    #         value2 = self.list[row].info[0]
    #         print('ID：' + str(value2) + '的' + columnname + '更新为' + value1)

    #         if columnname=="姓名" and value1=="":
    #             db = pymysql.connect(host=DBHOST, user=DBUSER, password=DBPASS, database=DBNAME)
    #             cursor = db.cursor()
    #             cursor.execute("delete from table1 where id=%s", ["{}".format(value2), ])
    #             db.commit()  # 提交命令
    #             if self.search_state==0:
    #                 self.search1()
    #             else:
    #                 self.search2()
    #             cursor.close()
    #             db.close()
    #             return


    #         db = pymysql.connect(host=DBHOST, user=DBUSER, password=DBPASS, database=DBNAME)
    #         cursor = db.cursor()
    #         try:
    #             sql = 'UPDATE TABLE1 SET ' + columnname + ' = \'' + value1 + '\' WHERE ID = ' + ' \'' + str(value2) + '\''
    #             cursor.execute(sql)
    #             db.commit()
    #             print("更新成功")
    #         except pymysql.err as e:
    #             print('更新失败')
    #             db.rollback()

    # def remove_all(self):
    #     predict.create_table()
    #     if self.search_state == 0:
    #         self.search1()
    #     else:
    #         self.search2()

    def display1(self):
        # print('普通按钮被点击了')
        self.ui.stacks.setCurrentIndex(0)

    def display2(self):
        # print('高级按钮被点击了')
        self.ui.stacks.setCurrentIndex(1)

    def getfile(self, button):
        filename, filetype = QFileDialog.getOpenFileName(self.ui, "选取文件", "./data",
                                                         "Excel Files (*.xls *.xlsx)")
        if button.isChecked():
            self.ui.plainTextEdit.appendPlainText(f"需要读取的路径为:{filename}")
            self.ui.plainTextEdit.appendPlainText(f"文件格式为:{filetype}")
        button.toggle()

    def getpath(self):      # 读取路径
        self.ui.plainTextEdit.clear()
        filepath = QtWidgets.QFileDialog.getExistingDirectory(None, "请选择文件夹路径", "D:/")
        self.path = filepath
        self.ui.plainTextEdit.appendPlainText(f"选择的路径为：{filepath}")
        self.ui.getpathbutton.toggle()

    def storage(self):      # 识别提取并存入数据库
        if self.path == '':
            self.ui.plainTextEdit.appendPlainText("请先选择文件夹路径！")
            return
        # read_files2(self.path)
        self.ui.plainTextEdit.appendPlainText("导入成功！")
        self.path = ''

    def selectionchange1(self):     # 设置下拉框
        self.ui.list2.clear()
        if self.ui.list1.currentText() == '表1':
            self.ui.list2.addItems(['发作演变过程'])
            # self.ui.list2.addItems(['症状性癫痫', '发育迟缓', '抽动症', '注意缺陷多动障碍', '自闭症', '局灶运动性发作', '局灶非运动发作', '局灶性继发双侧强直_阵挛发作',
            #                         '全面性运动性发作', '全面性非运动性发作', '新生儿期起病', '婴儿期起病', '儿童期起病', '青少年_成年期起病', '与年龄无特殊关系的癫痫综合征',
            #                         '其他癫痫综合征'])
        if self.ui.list1.currentText() == '表2':
            self.ui.list2.addItems(['诱发因素', '简单感觉发作', '认知', '情绪或情感', '自主神经', '自动症', '运动型', '跌倒',
                                    '发作演变过程', '发作持续时间', '发作后表现', '发作频次', '伴发热'])
        if self.ui.list1.currentText() == '表3':
            self.ui.list2.addItems(['惊厥史', '有无新生儿惊厥', '有无热性惊厥史', '有手术史', '外伤史', '输血史', '预防接种史', '母孕年龄',
                                    '孕期疾病', '孕次产出', '出生体重', '分娩方式', '是否有出生窒息', '是否有重度黄疸', '羊水污染',
                                    '喂养困难', '呕吐', '腹泻', '生长发育史迟缓', '生长发育倒退', '生长发育里程碑', '亲属是否有癫痫病人',
                                    '父母是否有过热性惊厥', '父母是否近亲结婚', '遗传代谢疾病', '求学困难', '被过度保护'
                                    , '心理压力大', '头围', '色素沉积'])
        if self.ui.list1.currentText() == '表4':
            self.ui.list2.addItems(['血氨', '血乳酸', '血、尿代谢筛查', '电解质', '铜兰蛋白', '脑脊液', '基因检查', '头部CT',
                                    '头部MRI', '头皮脑电图', '抗癫痫药物', '生酮饮食', '癫痫外科'])



app = QApplication([])
apply_stylesheet(app, "light_blue.xml", invert_secondary=True)
win = TestWin()
win.ui.show()
app.exec_()