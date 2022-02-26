import sys
from PyQt5.QtWidgets import QApplication,QWidget
from ui.YCYMainWindow import YCYMainWindow
import pydicom

if __name__=="__main__":
    app=QApplication(sys.argv)
    
    curMonitorNum = app.desktop().primaryScreen()#获主显示屏对象
    screenRect = app.desktop().screenGeometry(curMonitorNum)#获得主显示屏的尺寸

    mainWindow = YCYMainWindow(screenRect.width(),screenRect.height())
    mainWindow.show()
    sys.exit(app.exec_())

