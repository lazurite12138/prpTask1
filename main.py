import sys
from PyQt5.QtWidgets import QApplication,QWidget
from ui.YCYMainWindow import YCYMainWindow
if __name__=="__main__":
    app=QApplication(sys.argv)

    mainWindow = YCYMainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
