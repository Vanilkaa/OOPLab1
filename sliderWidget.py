import PySide6.QtWidgets

from ui_sliderWidget import Ui_SliderWidget

class SliderWidget(PySide6.QtWidgets.QWidget, Ui_SliderWidget):
    def __init__(self,app):
        super().__init__()
        self.setupUi(self)
        self.app = app

        self.horizontalSlider.valueChanged.connect(self.changeLabel)
        self.okBtn.clicked.connect(self.close)
        self.cancelBtn.clicked.connect(self.close)

    def changeLabel(self):
        self.label.setText(str(self.horizontalSlider.value()))
