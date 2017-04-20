import sys
import os
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QVBoxLayout,QHBoxLayout,QPushButton,QMainWindow,QLineEdit,QLabel
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import Qt

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'ChatBot'
        #self.statusMessage = '   Type Your Message...'
        self.top = 200
        self.left = 550
        self.height = 700
        self.width = 500
        self.initUI()  # next method call

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        #self.statusBar().showMessage(self.statusMessage)

        # initializations
        Message = QLineEdit(self)
        Message.setFixedWidth(450)
        Username = QLabel(self)
        User = QLabel(self)
        Userface = QPixmap('smiley_logo.png')
        User.setPixmap()

        Enter = QLabel(self)
        EnterLogo = QPixmap('EnterIcon.png')
        Enter.setPixmap(EnterLogo)
        h_box_Message = QHBoxLayout()
        h_box_Message.addWidget(Message)
        h_box_Message.addWidget(Enter)
        h_box_Message.addStretch()

        Message.move(10,650)
        Enter.move(465,650)
        self.show()


if __name__=='__main__':
    app = QApplication(sys.argv)
    path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'ICON.png')
    app.setWindowIcon(QIcon(path))
    ex = App() #calls App class
    sys.exit(app.exec_())
