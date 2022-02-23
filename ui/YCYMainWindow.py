from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class YCYMainWindow(QWidget):
    def __init__(self,parent=None):
        QMainWindow.__init__(self,parent)
        self.initUI()

    def initUI(self):
        self.createHboxGroupBox()#下方为水平布局
        mainLayout = QVBoxLayout()

        mainLayout.addWidget(self.Table())  # 在主页面插入表格
        mainLayout.addLayout(self.createHboxGroupBox())  # 再整体插入下方的水平布局
        self.setLayout(mainLayout)

        self.setGeometry(460, 230, 1000, 600)
        self.setWindowTitle('DICOM')

    def createHboxGroupBox(self):
        layout=QHBoxLayout()
        #搜索框
        searchLineEdit=QLineEdit()
        searchLineEdit.setPlaceholderText("Find text...")
        #打开文件和关闭窗口
        OpenBtn=QPushButton("File")
        CloseBtn=QPushButton("Close")

        layout.addWidget(searchLineEdit,2)
        layout.addStretch(5)
        layout.addWidget(OpenBtn,1)
        layout.addWidget(CloseBtn,1)

        return layout

    def Table(self):
        table=QTableWidget(100,6)#创建表格,这里后续要改为行数与文件数相同
        table.setFrameShape(QFrame.NoFrame)#无边框的表格
        table.horizontalHeader().setFixedHeight(50)#表头高度
        table.horizontalHeader().setSectionResizeMode(5,QHeaderView.Stretch)  # 设置第6列宽度自动调整，充满屏幕
        table.horizontalHeader().setStretchLastSection(True)  #设置最后一列拉伸至最大列无限延伸
        table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置不可选择单个单元格，只可选择一行。
        table.setColumnCount(6)  #设置表格一共有6列
        table.setHorizontalHeaderLabels(['Tag ID','VR','VM','Length','Description','Value'])  # 设置表头文字
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)  #设置表格不可更改
        table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置不可选择单个单元格，只可选择一行。
        table.verticalHeader().setVisible(False)
        table.setShowGrid(False)
        return table





