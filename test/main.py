import threading
import time
from PyQt5 import QtWidgets
import sys

def start_gui():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.resize(800, 500)
    txt = QtWidgets.QTextEdit(window)
    txt.resize(800, 495)
    send_txt(txt)
    window.show()
    sys.exit(app.exec_())

def send_txt(txt):
    txt.setText("Hello World\n")
    time.sleep(1)

thread1 = threading.Thread(target=start_gui)
thread2 = threading.Thread(target=send_txt)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
