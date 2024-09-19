import sys
from PySide6.QtWidgets import QApplication

from mainWindow import MainWindow
from sliderWidget import SliderWidget
from nextWidget import NextWidget
from prevWidget import PrevWidget

def closeApp(event):
    sliderWidget.close()
    event.accept()

def showSlider():
    try:
        sliderWidget.horizontalSlider.setValue(int(mainWindow.label.text()))
    except ValueError:
        pass
    nextWidget.close()
    prevWidget.close()
    sliderWidget.show()

def showNext():
    sliderWidget.close()
    nextWidget.show()

def showPrev():
    sliderWidget.close()
    prevWidget.show()

def showWidget():
    if mainWindow.comboBox.currentIndex():
        showNext()
        pass
    else: 
        showSlider()

def displayNumber():
    mainWindow.label.setText(str(sliderWidget.horizontalSlider.value()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    app.aboutToQuit.connect(closeApp)

    sliderWidget = SliderWidget(app)
    sliderWidget.okBtn.clicked.connect(displayNumber)

    nextWidget = NextWidget(app)
    nextWidget.nextBtn.clicked.connect(showPrev)
    prevWidget = PrevWidget(app)
    prevWidget.prevBtn.clicked.connect(showNext)

    mainWindow = MainWindow(app)
    mainWindow.comboBox.activated.connect(showWidget)
    mainWindow.show()

    sys.exit(app.exec())
