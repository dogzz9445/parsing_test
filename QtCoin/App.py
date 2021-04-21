from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

if __name__ == '__main__':
    app = QApplication(sys.argv)

    QApplication.setQuitOnLastWindowClosed(False)

    window = Window()
    window.show()

    sys.exit(app.exec_())