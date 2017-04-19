import sys
import os
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QLabel,QLineEdit,QPushButton
from PyQt5.QtGui import QIcon,QPixmap
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

        # declarations
        welcome = QLabel(self)
        botface = QLabel(self)
        UserNameLabel = QLabel(self)
        UserNameTextBox = QLineEdit(self)
        PasswordLabel = QLabel(self)
        PasswordTextBox = QLineEdit(self)
        confirmButton = QPushButton(self)

        # set them all
        botlogo = QPixmap('bot.png')
        welcome.setText('Please Register!')
        welcome.setAlignment(Qt.AlignLeft);
        botface.setPixmap(botlogo)
        confirmButton.setText("Confirm")

        # moving to appropriate positions
        UserNameLabel.move(10,100)
        UserNameTextBox.move(150,80)
        PasswordLabel.move(80,100)
        PasswordTextBox.move(150,100)
        welcome.move(200,40)
        botface.move(130,35)
        confirmButton.move(200,200)

        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'ICON.png')
    app.setWindowIcon(QIcon(path))
    ex = App() #calls App class
    sys.exit(app.exec_())
