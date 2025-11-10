# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connect_bt.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_connect_bt(object):
    def setupUi(self, connect_bt):
        if not connect_bt.objectName():
            connect_bt.setObjectName(u"connect_bt")
        connect_bt.resize(466, 370)
        connect_bt.setStyleSheet(u"background-color: rgb(58, 117, 176)")
        self.verticalLayout_5 = QVBoxLayout(connect_bt)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(connect_bt)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(connect_bt)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.label_3)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.widget = QWidget(connect_bt)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.label)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(120, 120))
        self.label_9.setPixmap(QPixmap(u"logo_lab.png"))
        self.label_9.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_9)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setMinimumSize(QSize(50, 0))

        self.horizontalLayout.addWidget(self.label_4)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.widget)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(connect_bt)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 30))

        self.verticalLayout_4.addWidget(self.label_5)

        self.id_bt = QLineEdit(connect_bt)
        self.id_bt.setObjectName(u"id_bt")
        self.id_bt.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.id_bt)

        self.label_6 = QLabel(connect_bt)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 20))

        self.verticalLayout_4.addWidget(self.label_6)

        self.btn_connect = QPushButton(connect_bt)
        self.btn_connect.setObjectName(u"btn_connect")
        self.btn_connect.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	ont: 75 8pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(199, 199, 199);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	ont: 75 8pt \"MS Shell Dlg 2\";\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_connect)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.retranslateUi(connect_bt)

        QMetaObject.connectSlotsByName(connect_bt)
    # setupUi

    def retranslateUi(self, connect_bt):
        connect_bt.setWindowTitle(QCoreApplication.translate("connect_bt", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("connect_bt", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">CENTRAL DE CONTROLE</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("connect_bt", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#ffffff;\">INTERFACE MIOCIN\u00c9TICA</span></p></body></html>", None))
        self.label.setText("")
        self.label_9.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Text, QColor("black"))  # texto digitado
        palette.setColor(QPalette.ColorRole.PlaceholderText, QColor("black"))  # placeholder
        self.id_bt.setPlaceholderText(QCoreApplication.translate("connect_bt", u"Insira o ID do bluetooth", None))
        self.id_bt.setPalette(palette)
        self.label_6.setText("")
        self.btn_connect.setText(QCoreApplication.translate("connect_bt", u"CONECTAR", None))
    # retranslateUi

