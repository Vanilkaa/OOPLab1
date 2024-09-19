import sys
from PySide6.QtWidgets import QMainWindow

from ui_mainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,app):
        super().__init__()
        self.setupUi(self)
        self.app = app

    def closeEvent(self, event):
        event.accept()
        sys.exit()
