import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
from PyQt5.QtGui import QIcon

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.show()

    if __init__='__main__':
        app = QApplication(sys.argv)
        ex = App()
        sys.exit(app.exec_())
