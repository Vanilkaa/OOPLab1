# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prevWidget.ui'
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

class Ui_prevWidget(object):
    def setupUi(self, prevWidget):
        if not prevWidget.objectName():
            prevWidget.setObjectName(u"prevWidget")
        prevWidget.resize(174, 42)
        prevWidget.setBaseSize(QSize(200, 50))
        self.horizontalLayout = QHBoxLayout(prevWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.prevBtn = QPushButton(prevWidget)
        self.prevBtn.setObjectName(u"prevBtn")

        self.horizontalLayout.addWidget(self.prevBtn)

        self.cancelBtn = QPushButton(prevWidget)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout.addWidget(self.cancelBtn)


        self.retranslateUi(prevWidget)

        QMetaObject.connectSlotsByName(prevWidget)
    # setupUi

    def retranslateUi(self, prevWidget):
        prevWidget.setWindowTitle(QCoreApplication.translate("prevWidget", u"Previous", None))
        self.prevBtn.setText(QCoreApplication.translate("prevWidget", u"Previous", None))
        self.cancelBtn.setText(QCoreApplication.translate("prevWidget", u"Cancel", None))
    # retranslateUi

