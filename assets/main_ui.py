# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import qrc1_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(949, 836)
        MainWindow.setStyleSheet(u"* {\n"
"	font-family:\u5fae\u8f6f\u96c5\u9ed1;\n"
"}\n"
".QPushButton[type=\"1\"]{\n"
"	color:rgb(255, 255, 255);\n"
"	background-color:\\rgb(43, 138, 255);\n"
"	font-size:17px;\n"
"	padding: 8px;\n"
"	font-weight: bold;\n"
"}\n"
".QPushButton[type=\"1\"][loc=\"left\"]{\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"}\n"
".QPushButton[type=\"1\"][loc=\"right\"]{\n"
"	border-top-right-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"}\n"
".QPushButton[type=\"2\"]{\n"
"	color:rgb(255, 255, 255);\n"
"	background-color:rgb(61, 209, 28);\n"
"	font-weight: bold;\n"
"	font-size:15px;\n"
"	padding: 10px 15px 10px 15px;\n"
"	border-top-right-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"	background-image:url(assets/search2.png);\n"
"	background-position:center;\n"
"	background-repeat:no-repeat;\n"
"}\n"
".QPushButton[type=\"3\"]{\n"
"	color:rgb(255, 255, 255);\n"
"	background-color:rgb(61, 209, 28);\n"
"	font-weight: bold;\n"
"	font-size:20px;\n"
"	padding: 10px 15px 10px 0px;"
                        "\n"
"	border-radius:10px;\n"
"	background-image:url(assets/search2.png);\n"
"	background-position:right;\n"
"	background-repeat:no-repeat;\n"
"}\n"
".QPushButton[type=\"4\"]{\n"
"	color:rgb(255, 255, 255);\n"
"	background-color:rgb(14, 74, 165);\n"
"	font-weight: bold;\n"
"	font-size:20px;\n"
"	padding: 10px 15px 10px 0px;\n"
"	border-radius:10px;\n"
"	background-position:right;\n"
"	background-repeat:no-repeat;\n"
"}\n"
".QPushButton[type=\"1\"]:checked{\n"
"	background-color:rgb(14, 74, 165);\n"
"}\n"
"#label {\n"
"	font-size:30px;\n"
"}\n"
"#groupBox_2 {\n"
"	border:0px solid\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 11, -1, -1)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_10 = QVBoxLayout(self.tab_3)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.tab_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(11, 30, 11, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 50, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.label)

        self.stack1Button = QPushButton(self.groupBox_2)
        self.stack1Button.setObjectName(u"stack1Button")
        self.stack1Button.setCursor(QCursor(Qt.PointingHandCursor))
        self.stack1Button.setCheckable(True)
        self.stack1Button.setChecked(True)
        self.stack1Button.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.stack1Button)

        self.stack2Button = QPushButton(self.groupBox_2)
        self.stack2Button.setObjectName(u"stack2Button")
        self.stack2Button.setCursor(QCursor(Qt.PointingHandCursor))
        self.stack2Button.setCheckable(True)
        self.stack2Button.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.stack2Button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 6)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(4, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 10)
        self.horizontalSpacer_2 = QSpacerItem(37, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.stacks = QStackedWidget(self.groupBox_2)
        self.stacks.setObjectName(u"stacks")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setBaseSize(QSize(0, 0))
        self.label_2.setStyleSheet(u"*{\n"
"	font-weight: bold;\n"
"}")

        self.verticalLayout_3.addWidget(self.label_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.searchtext1 = QLineEdit(self.page)
        self.searchtext1.setObjectName(u"searchtext1")
        self.searchtext1.setStyleSheet(u"*{\n"
"	font-size:25px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.searchtext1)

        self.searchButton = QPushButton(self.page)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchButton.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.searchButton)

        self.horizontalLayout_3.setStretch(0, 9)
        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_i1 = QLabel(self.page)
        self.label_i1.setObjectName(u"label_i1")
        self.label_i1.setStyleSheet(u"*{\n"
"	background-image:url(assets/i.png);\n"
"	background-position:center;\n"
"	background-repeat:no-repeat;\n"
"}")

        self.horizontalLayout_4.addWidget(self.label_i1)

        self.label_pt = QLabel(self.page)
        self.label_pt.setObjectName(u"label_pt")
        self.label_pt.setStyleSheet(u"*{\n"
"	color:rgb(118, 118, 118)\n"
"}")

        self.horizontalLayout_4.addWidget(self.label_pt)

        self.numlabel1 = QLabel(self.page)
        self.numlabel1.setObjectName(u"numlabel1")
        self.numlabel1.setLayoutDirection(Qt.LeftToRight)
        self.numlabel1.setStyleSheet(u"*{\n"
"	color:rgb(118, 118, 118)\n"
"}")
        self.numlabel1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.numlabel1)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 25)
        self.horizontalLayout_4.setStretch(2, 5)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_i1_2 = QLabel(self.page)
        self.label_i1_2.setObjectName(u"label_i1_2")
        self.label_i1_2.setStyleSheet(u"*{\n"
"	background-image:url(assets/i.png);\n"
"	background-position:center;\n"
"	background-repeat:no-repeat;\n"
"}")

        self.horizontalLayout_5.addWidget(self.label_i1_2)

        self.label_pt_2 = QLabel(self.page)
        self.label_pt_2.setObjectName(u"label_pt_2")
        self.label_pt_2.setStyleSheet(u"*{\n"
"	color:rgb(118, 118, 118)\n"
"}")

        self.horizontalLayout_5.addWidget(self.label_pt_2)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 30)

        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 143, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pushButton_3 = QPushButton(self.page)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.page)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.stacks.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_9 = QVBoxLayout(self.page_2)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, -1, 0, 30)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(20)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"*{\n"
"	font-weight: bold;\n"
"}")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 2)

        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.list1 = QComboBox(self.page_2)
        self.list1.addItem("")
        self.list1.addItem("")
        self.list1.addItem("")
        self.list1.addItem("")
        self.list1.setObjectName(u"list1")

        self.verticalLayout_5.addWidget(self.list1)


        self.horizontalLayout_11.addLayout(self.verticalLayout_5)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"*{\n"
"	font-weight: bold;\n"
"}")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 2)

        self.verticalLayout_7.addLayout(self.horizontalLayout_8)

        self.list2 = QComboBox(self.page_2)
        self.list2.addItem("")
        self.list2.addItem("")
        self.list2.addItem("")
        self.list2.addItem("")
        self.list2.addItem("")
        self.list2.addItem("")
        self.list2.addItem("")
        self.list2.addItem("")
        self.list2.addItem("")
        self.list2.addItem("")
        self.list2.addItem("")
        self.list2.addItem("")
        self.list2.addItem("")
        self.list2.addItem("")
        self.list2.addItem("")
        self.list2.addItem("")
        self.list2.setObjectName(u"list2")

        self.verticalLayout_7.addWidget(self.list2)


        self.horizontalLayout_11.addLayout(self.verticalLayout_7)


        self.verticalLayout_9.addLayout(self.horizontalLayout_11)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"*{\n"
"	font-weight: bold;\n"
"}")

        self.horizontalLayout_13.addWidget(self.label_5)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_9)


        self.verticalLayout_8.addLayout(self.horizontalLayout_13)

        self.searchtext2 = QLineEdit(self.page_2)
        self.searchtext2.setObjectName(u"searchtext2")
        self.searchtext2.setStyleSheet(u"*{\n"
"	font-size:25px;\n"
"}")

        self.verticalLayout_8.addWidget(self.searchtext2)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.searchButton_3 = QPushButton(self.page_2)
        self.searchButton_3.setObjectName(u"searchButton_3")
        self.searchButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchButton_3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_12.addWidget(self.searchButton_3)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_8)

        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 3)

        self.verticalLayout_9.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_i1_3 = QLabel(self.page_2)
        self.label_i1_3.setObjectName(u"label_i1_3")
        self.label_i1_3.setStyleSheet(u"*{\n"
"	background-image:url(assets/i.png);\n"
"	background-position:center;\n"
"	background-repeat:no-repeat;\n"
"}")

        self.horizontalLayout_9.addWidget(self.label_i1_3)

        self.label_pt_3 = QLabel(self.page_2)
        self.label_pt_3.setObjectName(u"label_pt_3")
        self.label_pt_3.setStyleSheet(u"*{\n"
"	color:rgb(118, 118, 118)\n"
"}")

        self.horizontalLayout_9.addWidget(self.label_pt_3)

        self.numlabel1_2 = QLabel(self.page_2)
        self.numlabel1_2.setObjectName(u"numlabel1_2")
        self.numlabel1_2.setLayoutDirection(Qt.LeftToRight)
        self.numlabel1_2.setStyleSheet(u"*{\n"
"	color:rgb(118, 118, 118)\n"
"}")
        self.numlabel1_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.numlabel1_2)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 25)
        self.horizontalLayout_9.setStretch(2, 5)

        self.verticalLayout_9.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_i1_4 = QLabel(self.page_2)
        self.label_i1_4.setObjectName(u"label_i1_4")
        self.label_i1_4.setStyleSheet(u"*{\n"
"	background-image:url(assets/i.png);\n"
"	background-position:center;\n"
"	background-repeat:no-repeat;\n"
"}")

        self.horizontalLayout_10.addWidget(self.label_i1_4)

        self.label_pt_4 = QLabel(self.page_2)
        self.label_pt_4.setObjectName(u"label_pt_4")
        self.label_pt_4.setStyleSheet(u"*{\n"
"	color:rgb(118, 118, 118)\n"
"}")

        self.horizontalLayout_10.addWidget(self.label_pt_4)

        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 30)

        self.verticalLayout_9.addLayout(self.horizontalLayout_10)

        self.pushButton_4 = QPushButton(self.page_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_9.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.page_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_9.addWidget(self.pushButton_5)

        self.verticalLayout_9.setStretch(0, 2)
        self.verticalLayout_9.setStretch(1, 3)
        self.verticalLayout_9.setStretch(2, 2)
        self.verticalLayout_9.setStretch(3, 1)
        self.verticalLayout_9.setStretch(4, 1)
        self.stacks.addWidget(self.page_2)

        self.horizontalLayout_2.addWidget(self.stacks)

        self.horizontalSpacer_4 = QSpacerItem(158, 292, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 8)
        self.horizontalLayout_2.setStretch(2, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout_10.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.tab_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(11, 0, 11, 0)
        self.table = QTableWidget(self.groupBox_3)
        if (self.table.columnCount() < 7):
            self.table.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.table.setObjectName(u"table")
        self.table.setDefaultDropAction(Qt.IgnoreAction)
        self.table.horizontalHeader().setStretchLastSection(False)

        self.verticalLayout_2.addWidget(self.table)

        self.verticalLayout_2.setStretch(0, 10)

        self.verticalLayout_10.addWidget(self.groupBox_3)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_6 = QVBoxLayout(self.tab_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(250, 100, 250, 50)
        self.getpathbutton = QPushButton(self.tab_4)
        self.getpathbutton.setObjectName(u"getpathbutton")
        self.getpathbutton.setCheckable(True)

        self.verticalLayout_15.addWidget(self.getpathbutton)

        self.pushButton = QPushButton(self.tab_4)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_15.addWidget(self.pushButton)

        self.label_4 = QLabel(self.tab_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_4)


        self.verticalLayout_6.addLayout(self.verticalLayout_15)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.plainTextEdit = QPlainTextEdit(self.tab_4)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setProperty("tabStopWidth", 80)

        self.verticalLayout_13.addWidget(self.plainTextEdit)


        self.verticalLayout_6.addLayout(self.verticalLayout_13)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.verticalLayout_6.setStretch(0, 4)
        self.verticalLayout_6.setStretch(1, 3)
        self.verticalLayout_6.setStretch(2, 3)
        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 949, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.stacks.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_2.setTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u75c5\u4eba", None))
        self.stack1Button.setText(QCoreApplication.translate("MainWindow", u"\u666e\u901a", None))
        self.stack1Button.setProperty("type", QCoreApplication.translate("MainWindow", u"1", None))
        self.stack1Button.setProperty("loc", QCoreApplication.translate("MainWindow", u"left", None))
        self.stack2Button.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u7ea7", None))
        self.stack2Button.setProperty("type", QCoreApplication.translate("MainWindow", u"1", None))
        self.stack2Button.setProperty("loc", QCoreApplication.translate("MainWindow", u"right", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u5185\u5bb9", None))
        self.searchtext1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165...", None))
        self.searchButton.setText("")
        self.searchButton.setProperty("type", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_i1.setText("")
        self.label_pt.setText(QCoreApplication.translate("MainWindow", u"\u666e\u901a\u641c\u7d22\uff1a\u6839\u636e\u75c5\u6848\u53f7\u6216\u59d3\u540d\u6765\u641c\u7d22", None))
        self.numlabel1.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u7ed3\u679c\uff1a0\u4eba", None))
        self.label_i1_2.setText("")
        self.label_pt_2.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u7ea7\u641c\u7d22\uff1a\u6839\u636e\u67d0\u4e2a\u5b57\u6bb5\u6765\u641c\u7d22", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u9009\u4e2d", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u5168\u90e8\u5220\u9664", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u8868", None))
        self.list1.setItemText(0, QCoreApplication.translate("MainWindow", u"\u88681", None))
        self.list1.setItemText(1, QCoreApplication.translate("MainWindow", u"\u88682", None))
        self.list1.setItemText(2, QCoreApplication.translate("MainWindow", u"\u88683", None))
        self.list1.setItemText(3, QCoreApplication.translate("MainWindow", u"\u88684", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u5b57\u6bb5", None))
        self.list2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u75c7\u72b6\u6027\u766b\u75eb", None))
        self.list2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u53d1\u80b2\u8fdf\u7f13", None))
        self.list2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u62bd\u52a8\u75c7", None))
        self.list2.setItemText(3, QCoreApplication.translate("MainWindow", u"\u6ce8\u610f\u7f3a\u9677\u591a\u52a8\u969c\u788d", None))
        self.list2.setItemText(4, QCoreApplication.translate("MainWindow", u"\u81ea\u95ed\u75c7", None))
        self.list2.setItemText(5, QCoreApplication.translate("MainWindow", u"\u5c40\u7076\u8fd0\u52a8\u6027\u53d1\u4f5c", None))
        self.list2.setItemText(6, QCoreApplication.translate("MainWindow", u"\u5c40\u7076\u975e\u8fd0\u52a8\u53d1\u4f5c", None))
        self.list2.setItemText(7, QCoreApplication.translate("MainWindow", u"\u5c40\u7076\u6027\u7ee7\u53d1\u53cc\u4fa7\u5f3a\u76f4_\u9635\u631b\u53d1\u4f5c", None))
        self.list2.setItemText(8, QCoreApplication.translate("MainWindow", u"\u5168\u9762\u6027\u8fd0\u52a8\u6027\u53d1\u4f5c", None))
        self.list2.setItemText(9, QCoreApplication.translate("MainWindow", u"\u5168\u9762\u6027\u975e\u8fd0\u52a8\u6027\u53d1\u4f5c", None))
        self.list2.setItemText(10, QCoreApplication.translate("MainWindow", u"\u65b0\u751f\u513f\u671f\u8d77\u75c5", None))
        self.list2.setItemText(11, QCoreApplication.translate("MainWindow", u"\u5a74\u513f\u671f\u8d77\u75c5", None))
        self.list2.setItemText(12, QCoreApplication.translate("MainWindow", u"\u513f\u7ae5\u671f\u8d77\u75c5", None))
        self.list2.setItemText(13, QCoreApplication.translate("MainWindow", u"\u9752\u5c11\u5e74_\u6210\u5e74\u671f\u8d77\u75c5", None))
        self.list2.setItemText(14, QCoreApplication.translate("MainWindow", u"\u4e0e\u5e74\u9f84\u65e0\u7279\u6b8a\u5173\u7cfb\u7684\u766b\u75eb\u7efc\u5408\u5f81", None))
        self.list2.setItemText(15, QCoreApplication.translate("MainWindow", u"\u5176\u4ed6\u766b\u75eb\u7efc\u5408\u5f81", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u5185\u5bb9", None))
        self.searchButton_3.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
        self.searchButton_3.setProperty("type", QCoreApplication.translate("MainWindow", u"3", None))
        self.label_i1_3.setText("")
        self.label_pt_3.setText(QCoreApplication.translate("MainWindow", u"\u666e\u901a\u641c\u7d22\uff1a\u6839\u636e\u75c5\u6848\u53f7\u6216\u59d3\u540d\u6765\u641c\u7d22", None))
        self.numlabel1_2.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u7ed3\u679c\uff1a0\u4eba", None))
        self.label_i1_4.setText("")
        self.label_pt_4.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u7ea7\u641c\u7d22\uff1a\u6839\u636e\u67d0\u4e2a\u5b57\u6bb5\u6765\u641c\u7d22\uff08\u9ed8\u8ba4\u641c\u7d22\u8be5\u5b57\u6bb5\u975e\u7a7a\u7684\u75c5\u5386\uff09", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u9009\u4e2d", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u5168\u90e8", None))
        self.groupBox_3.setTitle("")
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u7b2c\u51e0\u6b21\u4f4f\u9662", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u75c5\u6848\u53f7", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u6027\u522b", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u5e74\u9f84", None));
        ___qtablewidgetitem5 = self.table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u7535\u8bdd", None));
        ___qtablewidgetitem6 = self.table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u8be6\u7ec6\u4fe1\u606f", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u75c5\u4eba", None))
        self.getpathbutton.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u75c5\u5386\u6240\u5728\u7684\u6587\u4ef6\u5939", None))
        self.getpathbutton.setProperty("type", QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u5165\u6570\u636e\u5e93", None))
        self.pushButton.setProperty("type", QCoreApplication.translate("MainWindow", u"4", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u8fc7\u7a0b\u8f83\u957f\uff0c\u8bf7\u8010\u5fc3\u7b49\u5f85", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u75c5\u5386", None))
    # retranslateUi

