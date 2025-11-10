# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSlider, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_Interface(object):
    def setupUi(self, Interface):
        if not Interface.objectName():
            Interface.setObjectName(u"Interface")
        Interface.resize(1179, 655)
        Interface.setStyleSheet(u"\n"
"background-color: rgb(58, 117, 176);")
        self.centralwidget = QWidget(Interface)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.btn_personalizado = QPushButton(self.frame)
        self.btn_personalizado.setObjectName(u"btn_personalizado")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_personalizado.sizePolicy().hasHeightForWidth())
        self.btn_personalizado.setSizePolicy(sizePolicy1)
        self.btn_personalizado.setMaximumSize(QSize(8777215, 16777215))
        self.btn_personalizado.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_personalizado.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_3.addWidget(self.btn_personalizado)

        self.btn_padronizado = QPushButton(self.frame)
        self.btn_padronizado.setObjectName(u"btn_padronizado")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_padronizado.sizePolicy().hasHeightForWidth())
        self.btn_padronizado.setSizePolicy(sizePolicy2)
        self.btn_padronizado.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_padronizado.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_3.addWidget(self.btn_padronizado)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_3.addWidget(self.frame)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy3)
        self.stackedWidget.setStyleSheet(u"QSlider#horizontalSlider::handle:horizontal {\n"
"    background-color: orange;   /* cor do c\u00edrculo */\n"
"    border-radius: 10px;        /* deixa redondo */\n"
"    width: 20px;                /* largura do handle */\n"
"    height: 20px;               /* altura do handle */\n"
"    margin: -5px 0;             /* centraliza em rela\u00e7\u00e3o \u00e0 barra */\n"
"}\n"
"")
        self.pg_personalizado = QWidget()
        self.pg_personalizado.setObjectName(u"pg_personalizado")
        self.verticalLayout_12 = QVBoxLayout(self.pg_personalizado)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_23 = QLabel(self.pg_personalizado)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_5.addWidget(self.label_23)

        self.widget = QWidget(self.pg_personalizado)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(77, 155, 232);")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.checkBox_1 = QCheckBox(self.widget)
        self.checkBox_1.setObjectName(u"checkBox_1")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.checkBox_1.setFont(font)
        self.checkBox_1.setStyleSheet(u"QCheckBox::indicator:checked {\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"    background-color: #ffaa7f;      /* caixa laranja */\n"
"    border: 2px solid #ff8800;      /* mesma cor da borda */\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: white;                   /* cor do texto */\n"
"    font-weight: bold;\n"
"}")

        self.verticalLayout_4.addWidget(self.checkBox_1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        font1 = QFont()
        font1.setFamilies([u"MS Shell Dlg 2"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_10.addWidget(self.label_10)

        self.comboBox_1 = QComboBox(self.widget)
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.setObjectName(u"comboBox_1")
        self.comboBox_1.setStyleSheet("""
QComboBox {
    color: black;                       /* texto visível na combobox */
    background-color: rgb(255, 255, 255); /* fundo da combobox */
}

QComboBox QAbstractItemView {            /* estilo do popup (lista) */
    color: black;                       /* cor do texto dos itens */
    background-color: white;            /* fundo do popup */
    selection-background-color: #3874f2; /* cor do item selecionado */
    selection-color: white;
}
""")

        self.horizontalLayout_10.addWidget(self.comboBox_1)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy4)
        font2 = QFont()
        font2.setFamilies([u"MS Shell Dlg 2"])
        font2.setBold(False)
        font2.setItalic(False)
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"font: 10\n"
"pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.label_11)

        self.amp_1 = QLabel(self.widget)
        self.amp_1.setObjectName(u"amp_1")

        self.horizontalLayout_9.addWidget(self.amp_1)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.amplitude_1 = QSlider(self.widget)
        self.amplitude_1.setObjectName(u"amplitude_1")
        self.amplitude_1.setEnabled(True)
        self.amplitude_1.setStyleSheet(u"QSlider#amplitude_1::handle:horizontal_1 {\n"
"    background-color: #ffaa7f;   /* cor do c\u00edrculo */\n"
"    border-radius: 10px;        /* deixa redondo */\n"
"    width: 20px;                /* largura do handle */\n"
"    height: 20px;               /* altura do handle */\n"
"    margin: -5px 0;             /* centraliza em rela\u00e7\u00e3o \u00e0 barra */\n"
"}\n"
"")
        self.amplitude_1.setMaximum(10)
        self.amplitude_1.setOrientation(Qt.Horizontal)

        self.verticalLayout_4.addWidget(self.amplitude_1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")
        sizePolicy4.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy4)
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"font: 10\n"
"pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_8.addWidget(self.label_12)

        self.freq_1 = QLabel(self.widget)
        self.freq_1.setObjectName(u"freq_1")

        self.horizontalLayout_8.addWidget(self.freq_1)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.frequencia_1 = QSlider(self.widget)
        self.frequencia_1.setObjectName(u"frequencia_1")
        self.frequencia_1.setEnabled(True)
        self.frequencia_1.setToolTipDuration(-3)
        self.frequencia_1.setStyleSheet(u"QSlider#frequencia_1::handle:horizontal {\n"
"    background-color:  #ffaa7f;   /* cor do c\u00edrculo */\n"
"    border-radius: 10px;        /* deixa redondo */\n"
"    width: 20px;                /* largura do handle */\n"
"    height: 20px;               /* altura do handle */\n"
"    margin: -5px 0;             /* centraliza em rela\u00e7\u00e3o \u00e0 barra */\n"
"}\n"
"")
        self.frequencia_1.setMaximum(20)
        self.frequencia_1.setSingleStep(1)
        self.frequencia_1.setOrientation(Qt.Horizontal)

        self.verticalLayout_4.addWidget(self.frequencia_1)


        self.horizontalLayout_5.addWidget(self.widget)

        self.widget_3 = QWidget(self.pg_personalizado)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"background-color: rgb(77, 155, 232);")
        self.verticalLayout_7 = QVBoxLayout(self.widget_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.checkBox_2 = QCheckBox(self.widget_3)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font)
        self.checkBox_2.setStyleSheet(u"QCheckBox::indicator:checked {\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"    background-color: #ffaa7f;      /* caixa laranja */\n"
"    border: 2px solid #ff8800;      /* mesma cor da borda */\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: white;                   /* cor do texto */\n"
"    font-weight: bold;\n"
"}")

        self.verticalLayout_7.addWidget(self.checkBox_2)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_19 = QLabel(self.widget_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)
        self.label_19.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_17.addWidget(self.label_19)

        self.comboBox_2 = QComboBox(self.widget_3)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setStyleSheet("""
QComboBox {
    color: black;                       /* texto visível na combobox */
    background-color: rgb(255, 255, 255); /* fundo da combobox */
}

QComboBox QAbstractItemView {            /* estilo do popup (lista) */
    color: black;                       /* cor do texto dos itens */
    background-color: white;            /* fundo do popup */
    selection-background-color: #3874f2; /* cor do item selecionado */
    selection-color: white;
}
""")

        self.horizontalLayout_17.addWidget(self.comboBox_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_20 = QLabel(self.widget_3)
        self.label_20.setObjectName(u"label_20")
        sizePolicy4.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy4)
        self.label_20.setFont(font2)
        self.label_20.setStyleSheet(u"font: 10\n"
"pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_18.addWidget(self.label_20)

        self.amp_2 = QLabel(self.widget_3)
        self.amp_2.setObjectName(u"amp_2")

        self.horizontalLayout_18.addWidget(self.amp_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_18)

        self.amplitude_2 = QSlider(self.widget_3)
        self.amplitude_2.setObjectName(u"amplitude_2")
        self.amplitude_2.setEnabled(True)
        self.amplitude_2.setStyleSheet(u"QSlider#amplitude_2::handle:horizontal_1 {\n"
"    background-color: #ffaa7f;   /* cor do c\u00edrculo */\n"
"    border-radius: 10px;        /* deixa redondo */\n"
"    width: 20px;                /* largura do handle */\n"
"    height: 20px;               /* altura do handle */\n"
"    margin: -5px 0;             /* centraliza em rela\u00e7\u00e3o \u00e0 barra */\n"
"}\n"
"")
        self.amplitude_2.setMaximum(10)
        self.amplitude_2.setOrientation(Qt.Horizontal)

        self.verticalLayout_7.addWidget(self.amplitude_2)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_21 = QLabel(self.widget_3)
        self.label_21.setObjectName(u"label_21")
        sizePolicy4.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy4)
        self.label_21.setFont(font2)
        self.label_21.setStyleSheet(u"font: 10\n"
"pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_19.addWidget(self.label_21)

        self.freq_2 = QLabel(self.widget_3)
        self.freq_2.setObjectName(u"freq_2")

        self.horizontalLayout_19.addWidget(self.freq_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_19)

        self.frequencia_2 = QSlider(self.widget_3)
        self.frequencia_2.setObjectName(u"frequencia_2")
        self.frequencia_2.setEnabled(True)
        self.frequencia_2.setToolTipDuration(-3)
        self.frequencia_2.setStyleSheet(u"QSlider#frequencia_2::handle:horizontal {\n"
"    background-color:  #ffaa7f;   /* cor do c\u00edrculo */\n"
"    border-radius: 10px;        /* deixa redondo */\n"
"    width: 20px;                /* largura do handle */\n"
"    height: 20px;               /* altura do handle */\n"
"    margin: -5px 0;             /* centraliza em rela\u00e7\u00e3o \u00e0 barra */\n"
"}\n"
"")
        self.frequencia_2.setMaximum(20)
        self.frequencia_2.setSingleStep(1)
        self.frequencia_2.setOrientation(Qt.Horizontal)

        self.verticalLayout_7.addWidget(self.frequencia_2)


        self.horizontalLayout_5.addWidget(self.widget_3)

        self.widget_2 = QWidget(self.pg_personalizado)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color: rgb(77, 155, 232);")
        self.verticalLayout_5 = QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.checkBox_3 = QCheckBox(self.widget_2)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setFont(font)
        self.checkBox_3.setStyleSheet(u"QCheckBox::indicator:checked {\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"    background-color: #ffaa7f;      /* caixa laranja */\n"
"    border: 2px solid #ff8800;      /* mesma cor da borda */\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: white;                   /* cor do texto */\n"
"    font-weight: bold;\n"
"}")

        self.verticalLayout_5.addWidget(self.checkBox_3)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_13 = QLabel(self.widget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_11.addWidget(self.label_13)

        self.comboBox_3 = QComboBox(self.widget_2)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setStyleSheet("""
QComboBox {
    color: black;                       /* texto visível na combobox */
    background-color: rgb(255, 255, 255); /* fundo da combobox */
}

QComboBox QAbstractItemView {            /* estilo do popup (lista) */
    color: black;                       /* cor do texto dos itens */
    background-color: white;            /* fundo do popup */
    selection-background-color: #3874f2; /* cor do item selecionado */
    selection-color: white;
}
""")

        self.horizontalLayout_11.addWidget(self.comboBox_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_14 = QLabel(self.widget_2)
        self.label_14.setObjectName(u"label_14")
        sizePolicy4.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy4)
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet(u"font: 10\n"
"pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_12.addWidget(self.label_14)

        self.amp_3 = QLabel(self.widget_2)
        self.amp_3.setObjectName(u"amp_3")

        self.horizontalLayout_12.addWidget(self.amp_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.amplitude_3 = QSlider(self.widget_2)
        self.amplitude_3.setObjectName(u"amplitude_3")
        self.amplitude_3.setEnabled(True)
        self.amplitude_3.setStyleSheet(u"QSlider#amplitude_3::handle:horizontal_1 {\n"
"    background-color: #ffaa7f;   /* cor do c\u00edrculo */\n"
"    border-radius: 10px;        /* deixa redondo */\n"
"    width: 20px;                /* largura do handle */\n"
"    height: 20px;               /* altura do handle */\n"
"    margin: -5px 0;             /* centraliza em rela\u00e7\u00e3o \u00e0 barra */\n"
"}\n"
"")
        self.amplitude_3.setMaximum(10)
        self.amplitude_3.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.amplitude_3)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_15 = QLabel(self.widget_2)
        self.label_15.setObjectName(u"label_15")
        sizePolicy4.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy4)
        self.label_15.setFont(font2)
        self.label_15.setStyleSheet(u"font: 10\n"
"pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_13.addWidget(self.label_15)

        self.freq_3 = QLabel(self.widget_2)
        self.freq_3.setObjectName(u"freq_3")

        self.horizontalLayout_13.addWidget(self.freq_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.frequencia_3 = QSlider(self.widget_2)
        self.frequencia_3.setObjectName(u"frequencia_3")
        self.frequencia_3.setEnabled(True)
        self.frequencia_3.setToolTipDuration(-3)
        self.frequencia_3.setStyleSheet(u"QSlider#frequencia_3::handle:horizontal {\n"
"    background-color:  #ffaa7f;   /* cor do c\u00edrculo */\n"
"    border-radius: 10px;        /* deixa redondo */\n"
"    width: 20px;                /* largura do handle */\n"
"    height: 20px;               /* altura do handle */\n"
"    margin: -5px 0;             /* centraliza em rela\u00e7\u00e3o \u00e0 barra */\n"
"}\n"
"")
        self.frequencia_3.setMaximum(20)
        self.frequencia_3.setSingleStep(1)
        self.frequencia_3.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.frequencia_3)


        self.horizontalLayout_5.addWidget(self.widget_2)

        self.widget_4 = QWidget(self.pg_personalizado)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"background-color: rgb(77, 155, 232);")
        self.verticalLayout_6 = QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.checkBox_4 = QCheckBox(self.widget_4)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setFont(font)
        self.checkBox_4.setStyleSheet(u"QCheckBox::indicator:checked {\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"    background-color: #ffaa7f;      /* caixa laranja */\n"
"    border: 2px solid #ff8800;      /* mesma cor da borda */\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: white;                   /* cor do texto */\n"
"    font-weight: bold;\n"
"}")

        self.verticalLayout_6.addWidget(self.checkBox_4)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_16 = QLabel(self.widget_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)
        self.label_16.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_14.addWidget(self.label_16)

        self.comboBox_4 = QComboBox(self.widget_4)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setStyleSheet("""
QComboBox {
    color: black;                       /* texto visível na combobox */
    background-color: rgb(255, 255, 255); /* fundo da combobox */
}

QComboBox QAbstractItemView {            /* estilo do popup (lista) */
    color: black;                       /* cor do texto dos itens */
    background-color: white;            /* fundo do popup */
    selection-background-color: #3874f2; /* cor do item selecionado */
    selection-color: white;
}
""")

        self.horizontalLayout_14.addWidget(self.comboBox_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_17 = QLabel(self.widget_4)
        self.label_17.setObjectName(u"label_17")
        sizePolicy4.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy4)
        self.label_17.setFont(font2)
        self.label_17.setStyleSheet(u"font: 10\n"
"pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_15.addWidget(self.label_17)

        self.amp_4 = QLabel(self.widget_4)
        self.amp_4.setObjectName(u"amp_4")

        self.horizontalLayout_15.addWidget(self.amp_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_15)

        self.amplitude_4 = QSlider(self.widget_4)
        self.amplitude_4.setObjectName(u"amplitude_4")
        self.amplitude_4.setEnabled(True)
        self.amplitude_4.setStyleSheet(u"QSlider#amplitude_4::handle:horizontal_1 {\n"
"    background-color: #ffaa7f;   /* cor do c\u00edrculo */\n"
"    border-radius: 10px;        /* deixa redondo */\n"
"    width: 20px;                /* largura do handle */\n"
"    height: 20px;               /* altura do handle */\n"
"    margin: -5px 0;             /* centraliza em rela\u00e7\u00e3o \u00e0 barra */\n"
"}\n"
"")
        self.amplitude_4.setMaximum(10)
        self.amplitude_4.setOrientation(Qt.Horizontal)

        self.verticalLayout_6.addWidget(self.amplitude_4)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_18 = QLabel(self.widget_4)
        self.label_18.setObjectName(u"label_18")
        sizePolicy4.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy4)
        self.label_18.setFont(font2)
        self.label_18.setStyleSheet(u"font: 10\n"
"pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_16.addWidget(self.label_18)

        self.freq_4 = QLabel(self.widget_4)
        self.freq_4.setObjectName(u"freq_4")

        self.horizontalLayout_16.addWidget(self.freq_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_16)

        self.frequencia_4 = QSlider(self.widget_4)
        self.frequencia_4.setObjectName(u"frequencia_4")
        self.frequencia_4.setEnabled(True)
        self.frequencia_4.setToolTipDuration(-3)
        self.frequencia_4.setStyleSheet(u"QSlider#frequencia_4::handle:horizontal {\n"
"    background-color:  #ffaa7f;   /* cor do c\u00edrculo */\n"
"    border-radius: 10px;        /* deixa redondo */\n"
"    width: 20px;                /* largura do handle */\n"
"    height: 20px;               /* altura do handle */\n"
"    margin: -5px 0;             /* centraliza em rela\u00e7\u00e3o \u00e0 barra */\n"
"}\n"
"")
        self.frequencia_4.setMaximum(20)
        self.frequencia_4.setSingleStep(1)
        self.frequencia_4.setOrientation(Qt.Horizontal)

        self.verticalLayout_6.addWidget(self.frequencia_4)


        self.horizontalLayout_5.addWidget(self.widget_4)

        self.label_25 = QLabel(self.pg_personalizado)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_5.addWidget(self.label_25)


        self.verticalLayout_12.addLayout(self.horizontalLayout_5)

        self.label_22 = QLabel(self.pg_personalizado)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_12.addWidget(self.label_22)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_40 = QLabel(self.pg_personalizado)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_6.addWidget(self.label_40)

        self.widget_5 = QWidget(self.pg_personalizado)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"background-color: rgb(77, 155, 232);")
        self.verticalLayout_8 = QVBoxLayout(self.widget_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.checkBox_5 = QCheckBox(self.widget_5)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setFont(font)
        self.checkBox_5.setStyleSheet(u"QCheckBox::indicator:checked {\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"    background-color: #ffaa7f;      /* caixa laranja */\n"
"    border: 2px solid #ff8800;      /* mesma cor da borda */\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: white;                   /* cor do texto */\n"
"    font-weight: bold;\n"
"}")

        self.verticalLayout_8.addWidget(self.checkBox_5)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_24 = QLabel(self.widget_5)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font1)
        self.label_24.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_20.addWidget(self.label_24)

        self.comboBox_5 = QComboBox(self.widget_5)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setStyleSheet("""
QComboBox {
    color: black;                       /* texto visível na combobox */
    background-color: rgb(255, 255, 255); /* fundo da combobox */
}

QComboBox QAbstractItemView {            /* estilo do popup (lista) */
    color: black;                       /* cor do texto dos itens */
    background-color: white;            /* fundo do popup */
    selection-background-color: #3874f2; /* cor do item selecionado */
    selection-color: white;
}
""")

        self.horizontalLayout_20.addWidget(self.comboBox_5)


        self.verticalLayout_8.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_26 = QLabel(self.widget_5)
        self.label_26.setObjectName(u"label_26")
        sizePolicy4.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy4)
        self.label_26.setFont(font2)
        self.label_26.setStyleSheet(u"font: 10\n"
"pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_21.addWidget(self.label_26)

        self.amp_5 = QLabel(self.widget_5)
        self.amp_5.setObjectName(u"amp_5")

        self.horizontalLayout_21.addWidget(self.amp_5)


        self.verticalLayout_8.addLayout(self.horizontalLayout_21)

        self.amplitude_5 = QSlider(self.widget_5)
        self.amplitude_5.setObjectName(u"amplitude_5")
        self.amplitude_5.setEnabled(True)
        self.amplitude_5.setStyleSheet(u"QSlider#amplitude_5::handle:horizontal_1 {\n"
"    background-color: #ffaa7f;   /* cor do c\u00edrculo */\n"
"    border-radius: 10px;        /* deixa redondo */\n"
"    width: 20px;                /* largura do handle */\n"
"    height: 20px;               /* altura do handle */\n"
"    margin: -5px 0;             /* centraliza em rela\u00e7\u00e3o \u00e0 barra */\n"
"}\n"
"")
        self.amplitude_5.setMaximum(10)
        self.amplitude_5.setOrientation(Qt.Horizontal)

        self.verticalLayout_8.addWidget(self.amplitude_5)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_27 = QLabel(self.widget_5)
        self.label_27.setObjectName(u"label_27")
        sizePolicy4.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy4)
        self.label_27.setFont(font2)
        self.label_27.setStyleSheet(u"font: 10\n"
"pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_22.addWidget(self.label_27)

        self.freq_5 = QLabel(self.widget_5)
        self.freq_5.setObjectName(u"freq_5")

        self.horizontalLayout_22.addWidget(self.freq_5)


        self.verticalLayout_8.addLayout(self.horizontalLayout_22)

        self.frequencia_5 = QSlider(self.widget_5)
        self.frequencia_5.setObjectName(u"frequencia_5")
        self.frequencia_5.setEnabled(True)
        self.frequencia_5.setToolTipDuration(-3)
        self.frequencia_5.setStyleSheet(u"QSlider#frequencia_5::handle:horizontal {\n"
"    background-color:  #ffaa7f;   /* cor do c\u00edrculo */\n"
"    border-radius: 10px;        /* deixa redondo */\n"
"    width: 20px;                /* largura do handle */\n"
"    height: 20px;               /* altura do handle */\n"
"    margin: -5px 0;             /* centraliza em rela\u00e7\u00e3o \u00e0 barra */\n"
"}\n"
"")
        self.frequencia_5.setMaximum(20)
        self.frequencia_5.setSingleStep(1)
        self.frequencia_5.setOrientation(Qt.Horizontal)

        self.verticalLayout_8.addWidget(self.frequencia_5)


        self.horizontalLayout_6.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.pg_personalizado)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"background-color: rgb(77, 155, 232);")
        self.verticalLayout_9 = QVBoxLayout(self.widget_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.checkBox_6 = QCheckBox(self.widget_6)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setFont(font)
        self.checkBox_6.setStyleSheet(u"QCheckBox::indicator:checked {\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"    background-color: #ffaa7f;      /* caixa laranja */\n"
"    border: 2px solid #ff8800;      /* mesma cor da borda */\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: white;                   /* cor do texto */\n"
"    font-weight: bold;\n"
"}")

        self.verticalLayout_9.addWidget(self.checkBox_6)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_28 = QLabel(self.widget_6)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font1)
        self.label_28.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_23.addWidget(self.label_28)

        self.comboBox_6 = QComboBox(self.widget_6)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setStyleSheet("""
QComboBox {
    color: black;                       /* texto visível na combobox */
    background-color: rgb(255, 255, 255); /* fundo da combobox */
}

QComboBox QAbstractItemView {            /* estilo do popup (lista) */
    color: black;                       /* cor do texto dos itens */
    background-color: white;            /* fundo do popup */
    selection-background-color: #3874f2; /* cor do item selecionado */
    selection-color: white;
}
""")

        self.horizontalLayout_23.addWidget(self.comboBox_6)


        self.verticalLayout_9.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_29 = QLabel(self.widget_6)
        self.label_29.setObjectName(u"label_29")
        sizePolicy4.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy4)
        self.label_29.setFont(font2)
        self.label_29.setStyleSheet(u"font: 10\n"
"pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_24.addWidget(self.label_29)

        self.amp_6 = QLabel(self.widget_6)
        self.amp_6.setObjectName(u"amp_6")

        self.horizontalLayout_24.addWidget(self.amp_6)


        self.verticalLayout_9.addLayout(self.horizontalLayout_24)

        self.amplitude_6 = QSlider(self.widget_6)
        self.amplitude_6.setObjectName(u"amplitude_6")
        self.amplitude_6.setEnabled(True)
        self.amplitude_6.setStyleSheet(u"QSlider#amplitude_6::handle:horizontal_1 {\n"
"    background-color: #ffaa7f;   /* cor do c\u00edrculo */\n"
"    border-radius: 10px;        /* deixa redondo */\n"
"    width: 20px;                /* largura do handle */\n"
"    height: 20px;               /* altura do handle */\n"
"    margin: -5px 0;             /* centraliza em rela\u00e7\u00e3o \u00e0 barra */\n"
"}\n"
"")
        self.amplitude_6.setMaximum(10)
        self.amplitude_6.setOrientation(Qt.Horizontal)

        self.verticalLayout_9.addWidget(self.amplitude_6)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_30 = QLabel(self.widget_6)
        self.label_30.setObjectName(u"label_30")
        sizePolicy4.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy4)
        self.label_30.setFont(font2)
        self.label_30.setStyleSheet(u"font: 10\n"
"pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_25.addWidget(self.label_30)

        self.freq_6 = QLabel(self.widget_6)
        self.freq_6.setObjectName(u"freq_6")

        self.horizontalLayout_25.addWidget(self.freq_6)


        self.verticalLayout_9.addLayout(self.horizontalLayout_25)

        self.frequencia_6 = QSlider(self.widget_6)
        self.frequencia_6.setObjectName(u"frequencia_6")
        self.frequencia_6.setEnabled(True)
        self.frequencia_6.setToolTipDuration(-3)
        self.frequencia_6.setStyleSheet(u"QSlider#frequencia_6::handle:horizontal {\n"
"    background-color:  #ffaa7f;   /* cor do c\u00edrculo */\n"
"    border-radius: 10px;        /* deixa redondo */\n"
"    width: 20px;                /* largura do handle */\n"
"    height: 20px;               /* altura do handle */\n"
"    margin: -5px 0;             /* centraliza em rela\u00e7\u00e3o \u00e0 barra */\n"
"}\n"
"")
        self.frequencia_6.setMaximum(20)
        self.frequencia_6.setSingleStep(1)
        self.frequencia_6.setOrientation(Qt.Horizontal)

        self.verticalLayout_9.addWidget(self.frequencia_6)


        self.horizontalLayout_6.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.pg_personalizado)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setStyleSheet(u"background-color: rgb(77, 155, 232);")
        self.verticalLayout_10 = QVBoxLayout(self.widget_7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.checkBox_7 = QCheckBox(self.widget_7)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setFont(font)
        self.checkBox_7.setStyleSheet(u"QCheckBox::indicator:checked {\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"    background-color: #ffaa7f;      /* caixa laranja */\n"
"    border: 2px solid #ff8800;      /* mesma cor da borda */\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: white;                   /* cor do texto */\n"
"    font-weight: bold;\n"
"}")

        self.verticalLayout_10.addWidget(self.checkBox_7)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_31 = QLabel(self.widget_7)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font1)
        self.label_31.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_26.addWidget(self.label_31)

        self.comboBox_7 = QComboBox(self.widget_7)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setStyleSheet("""
QComboBox {
    color: black;                       /* texto visível na combobox */
    background-color: rgb(255, 255, 255); /* fundo da combobox */
}

QComboBox QAbstractItemView {            /* estilo do popup (lista) */
    color: black;                       /* cor do texto dos itens */
    background-color: white;            /* fundo do popup */
    selection-background-color: #3874f2; /* cor do item selecionado */
    selection-color: white;
}
""")

        self.horizontalLayout_26.addWidget(self.comboBox_7)


        self.verticalLayout_10.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_32 = QLabel(self.widget_7)
        self.label_32.setObjectName(u"label_32")
        sizePolicy4.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy4)
        self.label_32.setFont(font2)
        self.label_32.setStyleSheet(u"font: 10\n"
"pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_27.addWidget(self.label_32)

        self.amp_7 = QLabel(self.widget_7)
        self.amp_7.setObjectName(u"amp_7")

        self.horizontalLayout_27.addWidget(self.amp_7)


        self.verticalLayout_10.addLayout(self.horizontalLayout_27)

        self.amplitude_7 = QSlider(self.widget_7)
        self.amplitude_7.setObjectName(u"amplitude_7")
        self.amplitude_7.setEnabled(True)
        self.amplitude_7.setStyleSheet(u"QSlider#amplitude_7::handle:horizontal_1 {\n"
"    background-color: #ffaa7f;   /* cor do c\u00edrculo */\n"
"    border-radius: 10px;        /* deixa redondo */\n"
"    width: 20px;                /* largura do handle */\n"
"    height: 20px;               /* altura do handle */\n"
"    margin: -5px 0;             /* centraliza em rela\u00e7\u00e3o \u00e0 barra */\n"
"}\n"
"")
        self.amplitude_7.setMaximum(10)
        self.amplitude_7.setOrientation(Qt.Horizontal)

        self.verticalLayout_10.addWidget(self.amplitude_7)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_33 = QLabel(self.widget_7)
        self.label_33.setObjectName(u"label_33")
        sizePolicy4.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy4)
        self.label_33.setFont(font2)
        self.label_33.setStyleSheet(u"font: 10\n"
"pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_28.addWidget(self.label_33)

        self.freq_7 = QLabel(self.widget_7)
        self.freq_7.setObjectName(u"freq_7")

        self.horizontalLayout_28.addWidget(self.freq_7)


        self.verticalLayout_10.addLayout(self.horizontalLayout_28)

        self.frequencia_7 = QSlider(self.widget_7)
        self.frequencia_7.setObjectName(u"frequencia_7")
        self.frequencia_7.setEnabled(True)
        self.frequencia_7.setToolTipDuration(-3)
        self.frequencia_7.setStyleSheet(u"QSlider#frequencia_7::handle:horizontal {\n"
"    background-color:  #ffaa7f;   /* cor do c\u00edrculo */\n"
"    border-radius: 10px;        /* deixa redondo */\n"
"    width: 20px;                /* largura do handle */\n"
"    height: 20px;               /* altura do handle */\n"
"    margin: -5px 0;             /* centraliza em rela\u00e7\u00e3o \u00e0 barra */\n"
"}\n"
"")
        self.frequencia_7.setMaximum(20)
        self.frequencia_7.setSingleStep(1)
        self.frequencia_7.setOrientation(Qt.Horizontal)

        self.verticalLayout_10.addWidget(self.frequencia_7)


        self.horizontalLayout_6.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.pg_personalizado)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"background-color: rgb(77, 155, 232);")
        self.verticalLayout_11 = QVBoxLayout(self.widget_8)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.checkBox_8 = QCheckBox(self.widget_8)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setFont(font)
        self.checkBox_8.setStyleSheet(u"QCheckBox::indicator:checked {\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"    background-color: #ffaa7f;      /* caixa laranja */\n"
"    border: 2px solid #ff8800;      /* mesma cor da borda */\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: white;                   /* cor do texto */\n"
"    font-weight: bold;\n"
"}")

        self.verticalLayout_11.addWidget(self.checkBox_8)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_34 = QLabel(self.widget_8)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font1)
        self.label_34.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_29.addWidget(self.label_34)

        self.comboBox_8 = QComboBox(self.widget_8)
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setStyleSheet("""
QComboBox {
    color: black;                       /* texto visível na combobox */
    background-color: rgb(255, 255, 255); /* fundo da combobox */
}

QComboBox QAbstractItemView {            /* estilo do popup (lista) */
    color: black;                       /* cor do texto dos itens */
    background-color: white;            /* fundo do popup */
    selection-background-color: #3874f2; /* cor do item selecionado */
    selection-color: white;
}
""")

        self.horizontalLayout_29.addWidget(self.comboBox_8)


        self.verticalLayout_11.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_35 = QLabel(self.widget_8)
        self.label_35.setObjectName(u"label_35")
        sizePolicy4.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy4)
        self.label_35.setFont(font2)
        self.label_35.setStyleSheet(u"font: 10\n"
"pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_30.addWidget(self.label_35)

        self.amp_8 = QLabel(self.widget_8)
        self.amp_8.setObjectName(u"amp_8")

        self.horizontalLayout_30.addWidget(self.amp_8)


        self.verticalLayout_11.addLayout(self.horizontalLayout_30)

        self.amplitude_8 = QSlider(self.widget_8)
        self.amplitude_8.setObjectName(u"amplitude_8")
        self.amplitude_8.setEnabled(True)
        self.amplitude_8.setStyleSheet(u"QSlider#amplitude_8::handle:horizontal_1 {\n"
"    background-color: #ffaa7f;   /* cor do c\u00edrculo */\n"
"    border-radius: 10px;        /* deixa redondo */\n"
"    width: 20px;                /* largura do handle */\n"
"    height: 20px;               /* altura do handle */\n"
"    margin: -5px 0;             /* centraliza em rela\u00e7\u00e3o \u00e0 barra */\n"
"}\n"
"")
        self.amplitude_8.setMaximum(10)
        self.amplitude_8.setOrientation(Qt.Horizontal)

        self.verticalLayout_11.addWidget(self.amplitude_8)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_36 = QLabel(self.widget_8)
        self.label_36.setObjectName(u"label_36")
        sizePolicy4.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy4)
        self.label_36.setFont(font2)
        self.label_36.setStyleSheet(u"font: 10\n"
"pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_31.addWidget(self.label_36)

        self.freq_8 = QLabel(self.widget_8)
        self.freq_8.setObjectName(u"freq_8")

        self.horizontalLayout_31.addWidget(self.freq_8)


        self.verticalLayout_11.addLayout(self.horizontalLayout_31)

        self.frequencia_8 = QSlider(self.widget_8)
        self.frequencia_8.setObjectName(u"frequencia_8")
        self.frequencia_8.setEnabled(True)
        self.frequencia_8.setToolTipDuration(-3)
        self.frequencia_8.setStyleSheet(u"QSlider#frequencia_8::handle:horizontal {\n"
"    background-color:  #ffaa7f;   /* cor do c\u00edrculo */\n"
"    border-radius: 10px;        /* deixa redondo */\n"
"    width: 20px;                /* largura do handle */\n"
"    height: 20px;               /* altura do handle */\n"
"    margin: -5px 0;             /* centraliza em rela\u00e7\u00e3o \u00e0 barra */\n"
"}\n"
"")
        self.frequencia_8.setMaximum(20)
        self.frequencia_8.setSingleStep(1)
        self.frequencia_8.setOrientation(Qt.Horizontal)

        self.verticalLayout_11.addWidget(self.frequencia_8)


        self.horizontalLayout_6.addWidget(self.widget_8)

        self.label_39 = QLabel(self.pg_personalizado)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_6.addWidget(self.label_39)


        self.verticalLayout_12.addLayout(self.horizontalLayout_6)

        self.stackedWidget.addWidget(self.pg_personalizado)
        self.pg_padronizado = QWidget()
        self.pg_padronizado.setObjectName(u"pg_padronizado")
        self.verticalLayout_14 = QVBoxLayout(self.pg_padronizado)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_37 = QLabel(self.pg_padronizado)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(40, 0))

        self.horizontalLayout_7.addWidget(self.label_37)

        self.widget_10 = QWidget(self.pg_padronizado)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy4.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy4)
        self.widget_10.setStyleSheet(u"background-color: rgb(77, 155, 232);")
        self.layoutWidget = QWidget(self.widget_10)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 30, 243, 151))
        self.verticalLayout_15 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.m_1 = QRadioButton(self.layoutWidget)
        self.m_1.setObjectName(u"m_1")
        self.m_1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")

        self.verticalLayout_15.addWidget(self.m_1)

        self.m_2 = QRadioButton(self.layoutWidget)
        self.m_2.setObjectName(u"m_2")
        self.m_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")

        self.verticalLayout_15.addWidget(self.m_2)

        self.m_3 = QRadioButton(self.layoutWidget)
        self.m_3.setObjectName(u"m_3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.m_3.sizePolicy().hasHeightForWidth())
        self.m_3.setSizePolicy(sizePolicy5)
        self.m_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")

        self.verticalLayout_15.addWidget(self.m_3)

        self.m_4 = QRadioButton(self.layoutWidget)
        self.m_4.setObjectName(u"m_4")
        self.m_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")

        self.verticalLayout_15.addWidget(self.m_4)


        self.horizontalLayout_7.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.pg_padronizado)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy4.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy4)
        self.widget_11.setStyleSheet(u"background-color: rgb(77, 155, 232);")
        self.layoutWidget1 = QWidget(self.widget_11)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 20, 200, 151))
        self.verticalLayout_13 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.m_7 = QRadioButton(self.layoutWidget1)
        self.m_7.setObjectName(u"m_7")
        self.m_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")

        self.verticalLayout_13.addWidget(self.m_7)

        self.m_5 = QRadioButton(self.layoutWidget1)
        self.m_5.setObjectName(u"m_5")
        self.m_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")

        self.verticalLayout_13.addWidget(self.m_5)

        self.m_6 = QRadioButton(self.layoutWidget1)
        self.m_6.setObjectName(u"m_6")
        sizePolicy5.setHeightForWidth(self.m_6.sizePolicy().hasHeightForWidth())
        self.m_6.setSizePolicy(sizePolicy5)
        self.m_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")

        self.verticalLayout_13.addWidget(self.m_6)

        self.m_8 = QRadioButton(self.layoutWidget1)
        self.m_8.setObjectName(u"m_8")
        self.m_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")

        self.verticalLayout_13.addWidget(self.m_8)


        self.horizontalLayout_7.addWidget(self.widget_11)

        self.label_38 = QLabel(self.pg_padronizado)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(40, 0))

        self.horizontalLayout_7.addWidget(self.label_38)


        self.verticalLayout_14.addLayout(self.horizontalLayout_7)

        self.stackedWidget.addWidget(self.pg_padronizado)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_4.addWidget(self.label_8)

        self.btn_connect2 = QPushButton(self.centralwidget)
        self.btn_connect2.setObjectName(u"btn_connect2")
        sizePolicy5.setHeightForWidth(self.btn_connect2.sizePolicy().hasHeightForWidth())
        self.btn_connect2.setSizePolicy(sizePolicy5)
        self.btn_connect2.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_4.addWidget(self.btn_connect2)

        self.btn_iniciar = QPushButton(self.centralwidget)
        self.btn_iniciar.setObjectName(u"btn_iniciar")
        sizePolicy5.setHeightForWidth(self.btn_iniciar.sizePolicy().hasHeightForWidth())
        self.btn_iniciar.setSizePolicy(sizePolicy5)
        self.btn_iniciar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_iniciar.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_4.addWidget(self.btn_iniciar)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(200, 0))
        self.label_3.setMaximumSize(QSize(10777215, 70))

        self.horizontalLayout_4.addWidget(self.label_3)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(90, 80))
        self.label_9.setPixmap(QPixmap(u"logo_lab.png"))
        self.label_9.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_9)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        Interface.setCentralWidget(self.centralwidget)

        self.retranslateUi(Interface)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Interface)
    # setupUi

    def retranslateUi(self, Interface):
        Interface.setWindowTitle(QCoreApplication.translate("Interface", u"MainWindow", None))
        self.label_5.setText("")
        self.label_2.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">CENTRAL DE CONTROLE</span></p></body></html>", None))
        self.label_6.setText("")
        self.label_4.setText("")
        self.btn_personalizado.setText(QCoreApplication.translate("Interface", u"MOVIMENTO PERSONALIZADO", None))
        self.btn_padronizado.setText(QCoreApplication.translate("Interface", u"MOVIMENTO PADRONIZADO", None))
        self.label_7.setText("")
        self.label_23.setText("")
        self.checkBox_1.setText(QCoreApplication.translate("Interface", u"Marcador Magn\u00e9tico 1", None))
        self.label_10.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:9pt;\">FORMA DE ONDA:</span></p></body></html>", None))
        self.comboBox_1.setItemText(0, QCoreApplication.translate("Interface", u"Rampa", None))
        self.comboBox_1.setItemText(1, QCoreApplication.translate("Interface", u"Senoide", None))

        self.label_11.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:10pt;\">AMPLITUDE:                                            </span></p></body></html>", None))
        self.amp_1.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">10</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:10pt;\">FREQU\u00caNCIA (Hz): </span></p></body></html>", None))
        self.freq_1.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">10</span></p></body></html>", None))
        self.checkBox_2.setText(QCoreApplication.translate("Interface", u"Marcador Magn\u00e9tico 2", None))
        self.label_19.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:9pt;\">FORMA DE ONDA:</span></p></body></html>", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Interface", u"Rampa", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Interface", u"Senoide", None))

        self.label_20.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:10pt;\">AMPLITUDE:                                            </span></p></body></html>", None))
        self.amp_2.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">10</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:10pt;\">FREQU\u00caNCIA (Hz): </span></p></body></html>", None))
        self.freq_2.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">10</span></p></body></html>", None))
        self.checkBox_3.setText(QCoreApplication.translate("Interface", u"Marcador Magn\u00e9tico 3", None))
        self.label_13.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:9pt;\">FORMA DE ONDA:</span></p></body></html>", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("Interface", u"Rampa", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Interface", u"Senoide", None))

        self.label_14.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:10pt;\">AMPLITUDE:                                            </span></p></body></html>", None))
        self.amp_3.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">10</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:10pt;\">FREQU\u00caNCIA (Hz): </span></p></body></html>", None))
        self.freq_3.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">10</span></p></body></html>", None))
        self.checkBox_4.setText(QCoreApplication.translate("Interface", u"Marcador Magn\u00e9tico 4", None))
        self.label_16.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:9pt;\">FORMA DE ONDA:</span></p></body></html>", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("Interface", u"Rampa", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("Interface", u"Senoide", None))

        self.label_17.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:10pt;\">AMPLITUDE:                                            </span></p></body></html>", None))
        self.amp_4.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">10</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:10pt;\">FREQU\u00caNCIA (Hz): </span></p></body></html>", None))
        self.freq_4.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">10</span></p></body></html>", None))
        self.label_25.setText("")
        self.label_22.setText("")
        self.label_40.setText("")
        self.checkBox_5.setText(QCoreApplication.translate("Interface", u"Marcador Magn\u00e9tico 5", None))
        self.label_24.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:9pt;\">FORMA DE ONDA:</span></p></body></html>", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("Interface", u"Rampa", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("Interface", u"Senoide", None))

        self.label_26.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:10pt;\">AMPLITUDE:                                            </span></p></body></html>", None))
        self.amp_5.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">10</span></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:10pt;\">FREQU\u00caNCIA (Hz): </span></p></body></html>", None))
        self.freq_5.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">10</span></p></body></html>", None))
        self.checkBox_6.setText(QCoreApplication.translate("Interface", u"Marcador Magn\u00e9tico 6", None))
        self.label_28.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:9pt;\">FORMA DE ONDA:</span></p></body></html>", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("Interface", u"Rampa", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("Interface", u"Senoide", None))

        self.label_29.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:10pt;\">AMPLITUDE:                                            </span></p></body></html>", None))
        self.amp_6.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">10</span></p></body></html>", None))
        self.label_30.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:10pt;\">FREQU\u00caNCIA (Hz): </span></p></body></html>", None))
        self.freq_6.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">10</span></p></body></html>", None))
        self.checkBox_7.setText(QCoreApplication.translate("Interface", u"Marcador Magn\u00e9tico 7", None))
        self.label_31.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:9pt;\">FORMA DE ONDA:</span></p></body></html>", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("Interface", u"Rampa", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("Interface", u"Senoide", None))

        self.label_32.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:10pt;\">AMPLITUDE:                                            </span></p></body></html>", None))
        self.amp_7.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">10</span></p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:10pt;\">FREQU\u00caNCIA (Hz): </span></p></body></html>", None))
        self.freq_7.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">10</span></p></body></html>", None))
        self.checkBox_8.setText(QCoreApplication.translate("Interface", u"Marcador Magn\u00e9tico 8", None))
        self.label_34.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:9pt;\">FORMA DE ONDA:</span></p></body></html>", None))
        self.comboBox_8.setItemText(0, QCoreApplication.translate("Interface", u"Rampa", None))
        self.comboBox_8.setItemText(1, QCoreApplication.translate("Interface", u"Senoide", None))

        self.label_35.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:10pt;\">AMPLITUDE:                                            </span></p></body></html>", None))
        self.amp_8.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">10</span></p></body></html>", None))
        self.label_36.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:10pt;\">FREQU\u00caNCIA (Hz): </span></p></body></html>", None))
        self.freq_8.setText(QCoreApplication.translate("Interface", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">10</span></p></body></html>", None))
        self.label_39.setText("")
        self.label_37.setText("")
        self.m_1.setText(QCoreApplication.translate("Interface", u"M\u00e3o Abrindo", None))
        self.m_2.setText(QCoreApplication.translate("Interface", u"M\u00e3o Fechando", None))
        self.m_3.setText(QCoreApplication.translate("Interface", u"Movimento de Pin\u00e7a", None))
        self.m_4.setText(QCoreApplication.translate("Interface", u"Movimento de agarre", None))
        self.m_7.setText(QCoreApplication.translate("Interface", u"Gesto: N\u00famero 1", None))
        self.m_5.setText(QCoreApplication.translate("Interface", u"Gesto: N\u00famero 2", None))
        self.m_6.setText(QCoreApplication.translate("Interface", u"Gesto: N\u00famero 3", None))
        self.m_8.setText(QCoreApplication.translate("Interface", u"Gesto: Beleza", None))
        self.label_38.setText("")
        self.label_8.setText("")
        self.btn_connect2.setText(QCoreApplication.translate("Interface", u"CONECTAR", None))
        self.btn_iniciar.setText(QCoreApplication.translate("Interface", u"INICIAR TESTE", None))
        self.label_3.setText("")
        self.label_9.setText("")
    # retranslateUi

