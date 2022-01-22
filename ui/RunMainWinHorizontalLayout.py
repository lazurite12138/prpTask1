import sys
import MainWinHorizontalLayout

from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__=="__main__":
    app=QApplication(sys.argv) #创建整个应用对象的程序
    mainWindow=QMainWindow()#创建主窗口

    ui=MainWinHorizontalLayout.Ui_MainWindow()#调用类
    ui.setupUi(mainWindow)#调用类中函数添加控件

    mainWindow.show()#显示窗口
    sys.exit(app.exec_())
