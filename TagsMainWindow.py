from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.Qt import *


class TagsWindow(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self, parent)
        self.setWindowTitle('DICOM Tags')
        #改一下icon地址
        self.setWindowIcon(QIcon(" "))
        self.resize(1500, 800)
        self.move(210, 100)

        self.initUI()


    def initUI(self):
        #查找框模块，后续要加入查找功能
        findText = QLineEdit(self)
        findText.setPlaceholderText("输入内容以查找...")

        #导入按钮模块，后需要加入导入功能
        imput = QPushButton('导入', self)
        imput.resize(imput.sizeHint())

        #退出按钮模块
        quit = QPushButton('关闭', self)
        quit.resize(quit.sizeHint())
        QToolTip.setFont(QFont('SansSerif', 10))
        quit.setToolTip('点击退出程序')
        quit.clicked.connect(QCoreApplication.instance().quit)

        #显示内容表格模块
        #一个设想：能不能动态地按照传入的文件数量，来确定表格的行数，再生成表格
        showContents = QTableWidget(20,6)
        showContents.verticalHeader().setVisible(False)
        showContents.setHorizontalHeaderLabels(['Tag ID', 'VR', 'VM', 'Length',
                                                'Discription', 'Value'])
        showContents.setEditTriggers(QAbstractItemView.NoEditTriggers)      #设置为只读模式
        #设置表头
        columnWidth = [120,50,50,100,300,1000]
        for i in range(0,6):
            showContents.setColumnWidth(i,columnWidth[i])
        font = QFont('微软雅黑', 10)
        font.setBold(True)       #设置字体加粗
        showContents.horizontalHeader().setFont(font)       #设置表头字体
        showContents.horizontalHeader().setFixedHeight(40)      #设置表头高度
        showContents.horizontalHeader().setStyleSheet('QHeaderView::section{background:grey}')

        #布局设置
        mainLayout = QVBoxLayout()
        hboxLayout = QHBoxLayout()
        hboxLayout.addWidget(findText)
        hboxLayout.addStretch(0.5)         #目的：缩短查找文本框
        hboxLayout.setSpacing(20)
        hboxLayout.addWidget(imput)
        hboxLayout.addWidget(quit)
        mainLayout.addWidget(showContents)
        mainLayout.addLayout(hboxLayout)
        # mainLayout.setContentsMargins(15, 15, 15, 15)  # 设置外边距，左上右下
        # mainLayout.setSpacing(30)  # 设置内边距

        self.setLayout(mainLayout)
