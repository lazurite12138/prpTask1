from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class YCYMainWindow(QWidget):

    def __init__(self,parent=None):
        QMainWindow.__init__(self,parent)
        self.path=None
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
        self.layout=QHBoxLayout()
        #搜索框
        self.searchLineEdit=QLineEdit()
        self.searchLineEdit.setPlaceholderText("Find text...")
        #打开文件和关闭窗口
        self.OpenBtn=QPushButton("Files")
        self.OpenBtn.clicked.connect(self.openfolder)#点击打开文件夹并获取路径
        self.CloseBtn=QPushButton("Close")
        self.CloseBtn.clicked.connect(self.close)#点击“close”关闭窗口

        self.layout.addWidget(self.searchLineEdit,2)
        self.layout.addStretch(5)
        self.layout.addWidget(self.OpenBtn,1)
        self.layout.addWidget(self.CloseBtn,1)

        return self.layout

    def Table(self):
        self.table=QTableWidget(100,6)#创建表格,这里后续要改为行数与文件数相同
        self.table.setFrameShape(QFrame.NoFrame)#无边框的表格
        self.table.horizontalHeader().setFixedHeight(50)#表头高度
        self.table.horizontalHeader().setSectionResizeMode(5,QHeaderView.Stretch)  # 设置第6列宽度自动调整，充满屏幕
        self.table.horizontalHeader().setStretchLastSection(True)  #设置最后一列拉伸至最大列无限延伸
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置不可选择单个单元格，只可选择一行。
        self.table.setColumnCount(6)  #设置表格一共有6列
        self.table.setHorizontalHeaderLabels(['Tag ID','VR','VM','Length','Description','Value'])  # 设置表头文字
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)  #设置表格不可更改
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置不可选择单个单元格，只可选择一行。
        self.table.verticalHeader().setVisible(False)
        self.table.setShowGrid(False)
        return self.table

    def openfolder(self):#点击“Files”打开文件夹
        filePath,filetype = QFileDialog.getOpenFileName(self, "选取文件", "","*.*")
        self.path=filePath#将文件路径赋给path

