from PySide6 import QtWidgets
from PySide6.QtCore import QItemSelectionModel, QModelIndex
from PySide6.QtWidgets import QTableWidgetItem, QCheckBox
from PySide6.QtWidgets import QMessageBox, QMainWindow, QAbstractItemView
from injector import inject
from network.model import Patient
from typing import Sequence
from config import settings
from ui.viewmodel import State, ViewModel
from assets.main_ui import Ui_MainWindow


class TestWin(QMainWindow):
    @inject
    def __init__(self, viewmodel: ViewModel):
        super().__init__()
        self.ui = Ui_MainWindow()
        # self.set_extra(settings.THEME_EXTRA)
        self.ui.setupUi(self)

        self.path = ''
        self.file_name = ""
        # self.search_state=0
        self.table_data_checkboxes: list[QCheckBox] = []
        
        self.viewmodel = viewmodel
        self.state = self.viewmodel.state
        self.state.subscribe(
            on_next=self.observe
        )
        
        

        self.ui.searchButton.clicked.connect(
            lambda: self.viewmodel.common_search(self.ui.searchtext1.text())
        )
        self.ui.searchButton_3.clicked.connect(
            lambda: self.viewmodel.advanced_search(
                query=self.ui.searchtext2.text(),
                field=self.ui.list2.currentText()
            )
        )

        self.ui.stack1Button.clicked.connect(self.display1)
        self.ui.stack2Button.clicked.connect(self.display2)

        self.ui.list1.currentIndexChanged.connect(self.selectionchange1)
        # self.ui.getpathbutton.clicked.connect(lambda: self.getfile(self.ui.getpathbutton))
        self.ui.getpathbutton.clicked.connect(self.getpath)
        def storage():  # 识别提取并存入数据库
            if not self.path:
                self.ui.plainTextEdit.appendPlainText("请先选择文件夹路径！")
                return
            res = self.viewmodel.upload_file(self.path)
            self.path = ''
            return res

        self.ui.pushButton.clicked.connect(storage)

        def update(item):
            if not self._refreshing:
                return self.viewmodel.update_field(
                    id=int(self.ui.table.item(item.row(), 0).text()),
                    field=settings.TABLE_COLUMNS[item.column()],
                    value=item.text(),
                )

        self.ui.table.itemChanged.connect(update)
        self.ui.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        m = QItemSelectionModel(self.ui.table.model())
        
        self.ui.table.setSelectionModel(m)
        def select(current: QModelIndex, last: QModelIndex):
            all_selected = all(m.isRowSelected(row) for row in range(self.ui.table.rowCount()))
            
            self.ui.select_all.setChecked(all_selected)

        m.currentRowChanged.connect(select)
        
        def select_all(checked):
            if checked:
                self.ui.table.selectAll() 
            else:
                self.ui.table.clearSelection()
        self.ui.select_all.toggled.connect(select_all)

        self.ui.delete_selected.clicked.connect(self.delete_selected)

        
        # self.ui.pushButton_2.clicked.connect(self.presenter.delete_all_patients)
        # self.ui.setWindowTitle('病历查询')
        # cnames = ['ID', "身份证号", '第几次住院', '姓名', '病案号', '性别', '年龄', '电话', '发作演变过程']
        self.ui.table.setColumnCount(len(settings.TABLE_COLUMNS))
        self.ui.table.setHorizontalHeaderLabels(settings.TABLE_COLUMNS)
        self._refreshing = False
        # self.list = []
        
        self.ui.export_selected.clicked.connect(self.export_selected_to_excel)
        
        self.ui.list1.setEnabled(False)
        
        self.ui.list2.clear()
        self.ui.list2.addItems(settings.ANN_SEARCH_FIELDS)
    
    def observe(self, state: State):
        self.ui.table.setEnabled(not state.is_loading)
        self.ui.loading_label.setVisible(state.is_loading)
        match state:
            case State(is_loading=True):
                pass
                
            case State(error_message=msg) if msg is not None:
                self.show_critical_message(msg)
                self.viewmodel.on_error_dismiss()
                
            case State(table_data=table_data, upload_success=uploaded):
                self.ui.table.setRowCount(0)
                self.show_patients_on_table(table_data)
                self.ui.numlabel1_2.setText(f'搜索结果：{len(table_data)}人')
                
                if uploaded:
                    self.ui.plainTextEdit.appendPlainText("导入成功！")
                    self.viewmodel.uploaded_shown()
                    
                
    
    def show_critical_message(self, msg: str):
        QMessageBox.critical(
            self,
            '错误',
            msg
        )
    
    def show_patients_on_table(self, data: Sequence[Patient]):
        self._refreshing = True
        self.table_data_checkboxes.clear()
        for row in range(len(data)):
            self.ui.table.insertRow(row)
            for column, value in enumerate(data[row].model_dump().values()):
                self.ui.table.setItem(row, column, QTableWidgetItem(str(value)))
        
        self._refreshing = False
    
    def get_selected(self) -> set[int]:
        return {
            int(self.ui.table.item(item.row(), 0).text()) for item in self.ui.table.selectedItems()
        }
    
    def delete_selected(self):
        ids = self.get_selected()
        if len(ids) != 0:
            return self.viewmodel.delete_patients(*ids)
    
    # def delete_all(self):
    #     ids = [
    #         int(self.ui.table.item(row, 0).text())
    #         for row in range(self.ui.table.rowCount())
    #     ]
    #     return self.viewmodel.delete_patients(*ids)
        

    def display1(self):
        # print('普通按钮被点击了')
        self.ui.stacks.setCurrentIndex(0)

    def display2(self):
        # print('高级按钮被点击了')
        self.ui.stacks.setCurrentIndex(1)

    def getpath(self):      # 读取路径
        self.ui.plainTextEdit.clear()
        filepath = QtWidgets.QFileDialog.getExistingDirectory(self, "请选择文件夹路径")
        self.path = filepath
        self.ui.plainTextEdit.appendPlainText(f"选择的路径为：{filepath}")
        self.ui.getpathbutton.toggle()

    def export_selected_to_excel(self):
        dir_path = QtWidgets.QFileDialog.getExistingDirectory(self, "请选择文件夹路径")
        ids = self.get_selected()
        if len(ids) != 0:
            return self.viewmodel.export_to_excel(dir_path, *ids)

    def selectionchange1(self):     # 设置下拉框
        self.ui.list2.clear()
        if self.ui.list1.currentText() == '表1':
            self.ui.list2.addItems(list(settings.ANN_SEARCH_FIELDS))
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
