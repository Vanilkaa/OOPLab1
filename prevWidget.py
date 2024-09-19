import PySide6.QtWidgets

from ui_prevWidget import Ui_prevWidget

class PrevWidget(PySide6.QtWidgets.QWidget, Ui_prevWidget):
    def __init__(self,app):
        super().__init__()
        self.setupUi(self)
        self.app = app

        self.cancelBtn.clicked.connect(self.close)
        self.prevBtn.clicked.connect(self.close)