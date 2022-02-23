import sys
from PyQt5.QtWidgets import *

from TagsMainWindow import TagsWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TagsWindow()
    window.show()
    sys.exit(app.exec_())