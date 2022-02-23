from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class YCYMainWindow(QWidget):
    def __init__(self,parent=None):
        QMainWindow.__init__(self,parent)
        self.initUI()

    def initUI(self):

        layout=QHBoxLayout()
        table=QTableWidget(6,6)#创建表格
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

        layout.addWidget(table)
        self.setLayout(layout)

        self.setGeometry(500,500,500,500)
        self.setWindowTitle('DICOM')
