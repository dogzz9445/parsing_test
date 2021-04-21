import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Common.WebSocketManager import *

class Window(QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__()

        self.thread = WebSocketManager("ws://echo.websocket.org/")
        self.thread.start()

    def initGuiComponents(self):
        myTextbox = QLineEdit(self)
        myTextbox.move(20, 20)
        myTextbox.resize(360,40)




if __name__ == '__main__':
    app = QApplication(sys.argv)

    # QApplication.setQuitOnLastWindowClosed(False)

    window = Window()
    window.show()

    sys.exit(app.exec_())