import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
# from PyQt5.QtGui import QIcon

if __name__=='__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(300,300)
    w.move(100,300)
    w.setWindowTitle('Trial')
    w.show()

    sys.exit(app.exec_())
