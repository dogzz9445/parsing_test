from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self, q):
        super(Window, self).__init__()

        self.setGeometry(200, 200, 400, 200)
        self.setWindowTilte("Coin App")
        
        self.thread = WebSocketManager("ws://echo.websocket.org/")
        self.thread.start()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)

    QApplication.setQuitOnLastWindowClosed(False)

    window = Window()
    window.show()

    sys.exit(app.exec_())