from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pydicom as pyd

class YCYMainWindow(QWidget):

    updateTableSignal = pyqtSignal(str)

    def __init__(self,parent=None):
        QMainWindow.__init__(self,parent)

        self.table = None

        self.updateTableSignal.connect(self.updateTable)

        self.tableHeaderDict = {
            'Tag ID': 0,
            'VR': 1,
            'VM': 2,
            'Description': 3,
            'Value': 4
        }

        self.initUI()

    def initUI(self):
        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(10,10,10,0)
        mainLayout.setSpacing(0)
        self.table = self.createTable()
        mainLayout.addWidget(self.table)  # 在主页面插入表格
        mainLayout.addLayout(self.createHboxGroupBoxLayout())  # 再整体插入下方的水平布局
        self.setLayout(mainLayout)

        self.setGeometry(460, 230, 1000, 600)
        self.setWindowTitle('DICOM')

    def createHboxGroupBoxLayout(self):
        layout=QHBoxLayout()
        layout.setContentsMargins(0,10,0,10)
        layout.setAlignment(Qt.AlignVCenter)
        #搜索框
        searchLineEdit=QLineEdit()

        searchLineEdit.setPlaceholderText("Find text...")
        #打开文件和关闭窗口
        OpenBtn=QPushButton("Files")
        OpenBtn.clicked.connect(self.openfolder)#点击打开文件夹并获取路径

        CloseBtn=QPushButton("Close")
        CloseBtn.clicked.connect(self.close)#点击“close”关闭窗口

        layout.addWidget(searchLineEdit,2)
        layout.addStretch(5)
        layout.addWidget(OpenBtn,1)
        layout.addWidget(CloseBtn,1)

        return layout

    def updateTable(self, filePath):
        self.table.clearContents()
        self.table.setRowCount(0)

        ds = pyd.read_file(filePath)

        def createItem(key, header):
            item = QTableWidgetItem()
            text = ''
            if header == 'Tag ID':
                text = str(ds[key].tag)
            elif header == 'VR':
                text = ds[key].VR
            elif header == 'VM':
                text = str(ds[key].VM)
            elif header == 'Description':
                text = ds[key].keyword
            elif header == 'Value':
                text = str(ds[key].value)
            item.setText(text)
            return item

        for i,key in enumerate(ds._dict.keys()):
            self.table.insertRow(i)  # 下加一行
            for header in self.tableHeaderDict.keys():
                newItem = createItem(key, header)
                self.table.setItem(i, self.tableHeaderDict[header], newItem)

        self.table.sortItems(0, Qt.AscendingOrder)

    def createTable(self):
        table=QTableWidget(0,len(self.tableHeaderDict.keys()))#创建表格,这里后续要改为行数与文件数相同
        table.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        table.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        table.setFrameShape(QFrame.NoFrame)#无边框的表格

        table.horizontalHeader().setFixedHeight(50)#表头高度
        table.horizontalHeader().resizeSection(0, 150)  # 依次设施列宽
        table.horizontalHeader().resizeSection(1, 50)
        table.horizontalHeader().resizeSection(2, 50)
        #self.table.horizontalHeader().resizeSection(3, 80)
        table.horizontalHeader().resizeSection(3, 200)
        table.horizontalHeader().resizeSection(4, 150)
        table.horizontalHeader().setSectionResizeMode(4,QHeaderView.Stretch)  # 设置第6列宽度自动调整，充满屏幕
        table.horizontalHeader().setStretchLastSection(True)  #设置最后一列拉伸至最大列无限延伸

        table.setHorizontalHeaderLabels(list(self.tableHeaderDict.keys()))  # 设置表头文字
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)  #设置表格不可更改
        table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置不可选择单个单元格，只可选择一行。
        table.verticalHeader().setVisible(False)
        table.setShowGrid(False)
        return table

    def openfolder(self):#点击“Files”打开文件夹
        filePath,_ = QFileDialog.getOpenFileName(self, "选取文件", "","*.*")
        self.updateTableSignal.emit(filePath)