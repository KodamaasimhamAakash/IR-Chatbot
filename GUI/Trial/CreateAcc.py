import sys
import os
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Create Account'
        self.statusMessage = 'Create Account...'
        self.top = 200
        self.left = 550
        self.height = 300
        self.width = 500
        self.initUI()  # next method call

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.statusBar().showMessage(self.statusMessage)
        welcome = QLabel(self);
        welcome.setText('Hello There...Please Register Yourself!')
        welcome.setWordWrap()
        welcome.setAlignment(Qt.AlignLeft);
        #welcome.move(200,40)
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'ICON.png')
    app.setWindowIcon(QIcon(path))
    ex = App() #calls App class
    sys.exit(app.exec_())
