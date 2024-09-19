import PySide6.QtWidgets

from ui_nextWidget import Ui_nextWidget

class NextWidget(PySide6.QtWidgets.QWidget, Ui_nextWidget):
    def __init__(self,app):
        super().__init__()
        self.setupUi(self)
        self.app = app

        self.cancelBtn.clicked.connect(self.close)
        self.nextBtn.clicked.connect(self.close)