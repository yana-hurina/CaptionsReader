# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
                               QLabel, QPushButton, QSizePolicy, QWidget)


class Ui_Dialog(object):
    def __init__(self):
        self.word_file = None
        self.process = None

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 100)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(600, 100))
        Dialog.setMaximumSize(QSize(600, 100))
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_17 = QLabel(Dialog)
        self.label_17.setObjectName(u"label_17")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy1)
        self.label_17.setMinimumSize(QSize(110, 25))
        self.label_17.setMaximumSize(QSize(16777215, 16777215))
        self.label_17.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_17, 0, 0, 1, 1)

        self.word_file = QComboBox(Dialog)
        self.word_file.setObjectName(u"word_file")
        self.word_file.setMinimumSize(QSize(0, 25))
        font = QFont()
        font.setStyleStrategy(QFont.PreferAntialias)
        self.word_file.setFont(font)

        self.gridLayout.addWidget(self.word_file, 0, 1, 1, 1)

        self.process = QPushButton(Dialog)
        self.process.setObjectName(u"process")
        self.process.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.process, 1, 0, 1, 2)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Captions Reader", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"Word with screenshots:", None))
        self.process.setText(QCoreApplication.translate("Dialog", u"PROCESS", None))
    # retranslateUi
