import sys

from PyQt5.QtWidgets import QApplication,QWidget

if __name__=="__main__":
    app=QApplication(sys.argv)
    w=QWidget()

    w.resize(800,500)
    w.move(500,500)

    w.setWindowTitle("第一个基于PyQt5的GUI")

    w.show()

    sys.exit(app.exec_())
