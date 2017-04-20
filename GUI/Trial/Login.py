import sys
import os
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QLabel,QLineEdit,QPushButton,QVBoxLayout,QHBoxLayout
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
        PasswordTextBox.setEchoMode(QLineEdit.Password)
        confirmButton = QPushButton(self)

        # set them all
        botlogo = QPixmap('bot.png')
        welcome.setText('Login Please!')
        welcome.setAlignment(Qt.AlignLeft);
        botface.setPixmap(botlogo)
        botface.setFixedWidth(100)
        botface.setFixedHeight(80)
        UserNameLabel.setText("UserName: ")
        PasswordLabel.setText("Password: ")
        confirmButton.setText("Confirm")


        # making a layout
        h_box_Label = QHBoxLayout()
        h_box_TextBox = QHBoxLayout()
        v_box = QVBoxLayout()

        h_box_Label.addWidget(UserNameLabel)
        h_box_Label.addStretch()
        h_box_TextBox.addWidget(UserNameTextBox)
        h_box_TextBox.addStretch()
        h_box_Label.addWidget(PasswordLabel)
        h_box_TextBox.addWidget(PasswordTextBox)
        v_box.addLayout(h_box_Label)
        v_box.addStretch()
        v_box.addLayout(h_box_TextBox)


        # moving to appropriate positions
        UserNameLabel.move(150,80)
        UserNameTextBox.move(300,80)
        PasswordLabel.move(150,130)
        PasswordTextBox.move(300,130)
        welcome.move(250,40)
        botface.move(180,10)
        confirmButton.move(200,200)

        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'ICON.png')
    app.setWindowIcon(QIcon(path))
    ex = App() #calls App class
    sys.exit(app.exec_())
