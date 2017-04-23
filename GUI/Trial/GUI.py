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
        self.width = 520
        self.initUI()  # next method call

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        #self.statusBar().showMessage(self.statusMessage)

        # initializations

        self.Message = QLineEdit(self)
        self.Message.setFixedWidth(450)
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
        
        self.enter = QPushButton('Enter',self)
        self.enter.setToolTip('Press to Enter Message')
        self.enter.setFixedWidth(50)
        self.enter.setShortcut('Enter')
        self.enter.clicked.connect(self.on_click)
        self.newMessageLabel = QLabel(self)
        self.Message.returnPressed.connect(self.enter.click)
        self.enter.setAutoDefault(True)


        h_box_Message = QHBoxLayout()
        h_box_User = QHBoxLayout()
        h_box_Message.addWidget(self.Message)
        h_box_Message.addWidget(self.enter)
        h_box_Message.addStretch()
        #h_box_User.addWidget(Username)
        #h_box_User.addWidget(User)
        h_box_User.addStretch()
        self.yaxis = 600
        self.count = 0
        self.
        self.Message.move(10,650)
        self.enter.move(465,650)



        #Username.move(370,10)
        #User.move(450,10)
        #Box.move(350,5)

        #self.fileUserPic()
        #self.messageUser()


    @pyqtSlot()
    def on_click(self):
        self.count + 1
        for
        self.newMessageLabel.setFixedWidth(450)
        self.newMessageLabel.move(10,self.yaxis)
        self.newMessageLabel.setStyleSheet('background-color:white')
        messageEntered = self.Message.text()
        self.newMessageLabel.setText(messageEntered);
        self.Message.clear()
        self.yaxis = self.yaxis - 50


if __name__=='__main__':
    app = QApplication(sys.argv)
    path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'ICON.png')
    app.setWindowIcon(QIcon(path))
    ex = App() #calls App class
    ex.show()
    sys.exit(app.exec_())
