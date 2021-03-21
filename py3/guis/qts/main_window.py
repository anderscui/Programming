# coding=utf-8

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QStatusBar, QToolBar, QMenuBar


class Window(QMainWindow):
    def __init__(self, parent=None, title='My Windows'):
        super().__init__(parent)

        self.setWindowTitle(title)
        self.setCentralWidget(QLabel('Central W'))

        self._createMenu()
        self._createToolBar()
        self._createStatusBar()

    def _createMenu(self):
        # menubar = QMenuBar()
        # self.layout().addWidget(menubar)
        # actionFile = menubar.addMenu('File')
        # menubar.addMenu('Help')

        self.menu = self.menuBar().addMenu('&Menu')
        self.menu.addAction('&Exit', self.close)

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Exit', self.close)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage('Look at this status...')
        self.setStatusBar(status)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
