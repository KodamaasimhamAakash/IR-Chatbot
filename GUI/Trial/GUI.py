import sys
import os
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QVBoxLayout,QHBoxLayout,QPushButton,QMainWindow,QLineEdit,QLabel,QFileDialog,QPushButton,QAction
from PyQt5.QtGui import QIcon,QPixmap,QFont
from PyQt5.QtCore import Qt,pyqtSlot

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
        '''Box = QLabel(self)                              # For Username
        Box.setStyleSheet('background-color: white;')
        Box.setFixedWidth(150)
        Box.setFixedHeight(50)
        Username = QLabel(self)
        Username.setFont(QFont('SansSerif',10))
        Username.setText('Username')
        User = QLabel(self)

        Userface = QPixmap('smiley_logo.png')
        User.setPixmap(Userface)
        User.setFixedHeight(40)'''

        #Enter = QLabel(self)
        #EnterLogo = QPixmap('EnterIcon.png')
        #Enter.setPixmap(EnterLogo)
        enter = QPushButton('Enter',self)
        enter.setToolTip('Press to Enter Message')
        enter.setFixedWidth(100)
        enter.setShortcut('Enter')
        enter.clicked.connect(self.on_click)
        h_box_Message = QHBoxLayout()
        h_box_User = QHBoxLayout()
        h_box_Message.addWidget(Message)
        h_box_Message.addWidget(enter)
        h_box_Message.addStretch()
        #h_box_User.addWidget(Username)
        #h_box_User.addWidget(User)
        h_box_User.addStretch()

        Message.move(10,650)
        enter.move(465,650)
        #Username.move(370,10)
        #User.move(450,10)
        #Box.move(350,5)

        #self.fileUserPic()
        #self.messageUser()
        self.show()

    @pyqtSlot()
    def on_click(self):
        




if __name__=='__main__':
    app = QApplication(sys.argv)
    path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'ICON.png')
    app.setWindowIcon(QIcon(path))
    ex = App() #calls App class
    sys.exit(app.exec_())
