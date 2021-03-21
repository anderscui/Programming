# coding=utf-8
import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget

app = QApplication(sys.argv)

# QWidget is the base class of all user interfaces objects in PyQt.
window = QWidget()
window.setWindowTitle('Calculator')
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)

# in PyQt5, you can use any widget as as top-level window, or even a button or a label.
msg_label = QLabel('<h1>Hello World</h1>', parent=window)
msg_label.move(60, 15)

window.show()

# Run you app's event loop (main loop)
sys.exit(app.exec_())
