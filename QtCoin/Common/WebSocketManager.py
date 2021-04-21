import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time
from PyQt5.QtCore import *

class WebSocketManager(QThread):
    def __init__(self, url: str, parent=None):
        super(WebSocketManager, self).__init__(parent)

        websocket.enableTrace(True)

        self.wsapp = websocket.WebSocketApp(
            url, 
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            on_ping=self.on_ping,
            on_pong=self.on_pong)

    def run(self):
        self.wsapp.run_forever(
            skip_utf8_validation=True,
            ping_interval=60, 
            ping_timeout=10)

    def on_message(self, wsapp, message):
        print(message)
        wsapp.close(status=websocket.STATUS_PROTOCOL_ERROR)

    def on_error(self, wsapp, error):
        print(error)

    def on_close(self, wsapp):
        print('### closed ###')

    def on_ping(self, wsapp, message):
        print("ping")
    
    def on_pong(self, wsapp, message):
        print("ping")