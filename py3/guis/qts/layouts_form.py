# coding=utf-8

import sys

from PyQt5.QtWidgets import QApplication, QFormLayout, QPushButton, QWidget, QLineEdit

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QHFormLayout')
layout = QFormLayout()

layout.addRow('Name:', QLineEdit())
layout.addRow('Age:', QLineEdit())
layout.addRow('Job:', QLineEdit())

window.setLayout(layout)
window.show()

sys.exit(app.exec_())
