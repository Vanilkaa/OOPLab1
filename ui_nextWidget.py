# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nextWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QWidget)

class Ui_nextWidget(object):
    def setupUi(self, nextWidget):
        if not nextWidget.objectName():
            nextWidget.setObjectName(u"nextWidget")
        nextWidget.resize(174, 42)
        nextWidget.setBaseSize(QSize(200, 50))
        self.horizontalLayout = QHBoxLayout(nextWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.nextBtn = QPushButton(nextWidget)
        self.nextBtn.setObjectName(u"nextBtn")

        self.horizontalLayout.addWidget(self.nextBtn)

        self.cancelBtn = QPushButton(nextWidget)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout.addWidget(self.cancelBtn)


        self.retranslateUi(nextWidget)

        QMetaObject.connectSlotsByName(nextWidget)
    # setupUi

    def retranslateUi(self, nextWidget):
        nextWidget.setWindowTitle(QCoreApplication.translate("nextWidget", u"Next", None))
        self.nextBtn.setText(QCoreApplication.translate("nextWidget", u"Next", None))
        self.cancelBtn.setText(QCoreApplication.translate("nextWidget", u"Cancel", None))
    # retranslateUi

